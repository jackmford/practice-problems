import json
import asyncio
import random
import time
import heapq

from redis import Redis
from rq import Queue
from prometheus_client import start_http_server, Counter, Histogram, Gauge


REDIS_CONN = Redis(host="redis", port=6379, decode_responses=True)

# Using a queue here but for multiple consumers could use
# Redis STREAM instead
queue = Queue(connection=REDIS_CONN)

QUEUE_NAME = "QUEUE"
POLL_TIME = 10
SEND_TIME = 15
PROMETHEUS_PORT = 8006

TRANSACTIONS_TO_SEND = {}

FAILED_TRANSACTIONS = Counter(
    "failed_poly_transactions",
    "Counter for transactions that are reported failed from Poly",
)
ACCEPTED_TRANSACTIONS = Counter(
    "accepted_poly_transactions",
    "Counter for transactions that are reported accepted from Poly",
)
REQUEST_DURATION = Histogram(
    "http_request_duration_seconds",
    "Duration of HTTP requests in seconds",
    buckets=[0.05, 0.1, 0.25, 0.5, 1.0, 2.5, 5.0, 10.0, 15.0, 20.0, 30.0, 60.0],
)
CURRENT_NONCE = Gauge("current_nonce_value", "Value of the redis nonce")
WALLET_NONCE = Gauge("wallet_nonce_value", "Value wallet nonce (remote)")
GAS_FEE = Gauge("base_gas_fee", "Current value of the gas fee")

TRANSACTION_MAX_RETRIES = 3
RETRY_BASE_DELAY = 0.25
DOG_TIMER = 60
        GAS_FEE.set(BASE_GAS_FEE)


async def claim_nonce():
    # Use incr for atomicity
    # Gets it and increments it, returns current nonce to send
    nonce = REDIS_CONN.incr("relayer_nonce") - 1
    CURRENT_NONCE.set(nonce)
    return nonce


async def get_wallet_nonce():
    # TODO: pull actual nonce
    # Ex. call
    # blockchain_nonce = web3.eth.get_transaction_count(RELAYER_ADDRESS, 'pending')

    # MOCK nonce get
    blockchain_nonce = random.randint(0, 1000)
    WALLET_NONCE.set(blockchain_nonce)
    # Only set it if Redis doesn't already have a higher number
    # setnx = set not exists
    REDIS_CONN.setnx("relayer_nonce", blockchain_nonce)


async def assign_nonce_to_transaction(tid):
    if tid in TRANSACTIONS_TO_SEND:
        # prevent assigning a transaction that already has a nonce, a new nonce (double spend)
        if "nonce" not in TRANSACTIONS_TO_SEND[tid]:
            TRANSACTIONS_TO_SEND[tid]["nonce"] = await claim_nonce()


async def poll_for_transactions():
    while True:
        item = REDIS_CONN.rpop(QUEUE_NAME)
        if item:
            print("Pulling transaction from queue")
            try:
                item_json = json.loads(item)  # type:ignore
                tid = item_json["transaction_id"]
                async with lock:
                    TRANSACTIONS_TO_SEND[tid] = item_json
                    TRANSACTIONS_TO_SEND[tid]["state"] = "PENDING"
                    TRANSACTIONS_TO_SEND[tid]["claimed_at"] = time.time()
                    await assign_nonce_to_transaction(tid)

            except Exception as e:
                print(f"Exception processing item {item}: {e}")  # type:ignore

        await asyncio.sleep(POLL_TIME)


# Mock API
async def poly_request():
    # Generate latency data for our histogram
    await asyncio.sleep(random.randint(0, 12))

    if random.random() < 0.3:
        return 500

    return 200


async def send_request(transaction_id):
    # these should all be sent async
    print(
        f"Sending {transaction_id} to Poly (Nonce {TRANSACTIONS_TO_SEND[transaction_id]['nonce']})..."
    )
    for attempt in range(TRANSACTION_MAX_RETRIES):
        try:
            with REQUEST_DURATION.time():
                response = await poly_request()

            # Use raise_for_status() on a real request
            if response == 200:
                # Transaction is "ACCEPTED", but not "FINALIZED" yet
                # Indexer service handles watching for FINALIZED and
                # Updating DB
                async with lock:
                    if transaction_id in TRANSACTIONS_TO_SEND:
                        del TRANSACTIONS_TO_SEND[transaction_id]
                        print(f"{transaction_id} accepted on attempt {attempt + 1}.")
                        ACCEPTED_TRANSACTIONS.inc()
                break
            else:
                raise Exception("Request to poly_request failed.")
        except Exception as e:
            FAILED_TRANSACTIONS.inc()
            if attempt == TRANSACTION_MAX_RETRIES - 1:
                print(
                    f"{transaction_id} attempt {attempt + 1}/{TRANSACTION_MAX_RETRIES} failed: {e}. Marking as failed in DB"
                )
                # Mark as failed in DB MOCK
                break

            print(
                f"{transaction_id} attempt {attempt + 1}/{TRANSACTION_MAX_RETRIES} failed: {e}. Retrying..."
            )

            # TRANSACTIONS_TO_SEND[transaction_id].setdefault("retries", 0)
            # TRANSACTIONS_TO_SEND[transaction_id]["retries"] += 1

            # exponential backoff
            delay = RETRY_BASE_DELAY * (2**attempt)
            # jitter
            delay *= random.uniform(0.8, 1.2)

            await asyncio.sleep(delay)


async def send_transactions_to_poly():
    while True:
        pending_to_send = []
        async with lock:
            # These keys should all be marked as IN PROGRESS so no other threads pick them up
            # Could use a temporary function scoped dict, copy them over, remove them from main, submit failed ones back onto main dict
            keys = list(TRANSACTIONS_TO_SEND.keys())
            for transaction_id in keys:
                if (
                    transaction_id in TRANSACTIONS_TO_SEND
                    and TRANSACTIONS_TO_SEND[transaction_id]["state"] == "PENDING"
                ):
                    TRANSACTIONS_TO_SEND[transaction_id]["state"] = "IN_PROGRESS"
                    pending_to_send.append(transaction_id)

        # use a minheap to order by nonce
        heap = []
        for tid in pending_to_send:
            heap.append([TRANSACTIONS_TO_SEND[tid]["nonce"], tid])
        heapq.heapify(heap)

        # 1 at a time approach
        # while heap:
        #    nonce, tid = heapq.heappop(heap)
        #    await send_request(tid)

        # Broadcast approach
        # tasks = []
        # for transaction_id in pending_to_send:
        #    tasks.append(send_request(transaction_id))

        # Broadcast approach with nonce order
        tasks = []
        while heap:
            nonce, tid = heapq.heappop(heap)
            tasks.append(send_request(tid))

        await asyncio.gather(*tasks)

        await asyncio.sleep(SEND_TIME)


# watcher should pick up transactions that are stuck and blocking and resubmit them
async def the_watcher_doggenstein():
    while True:
        async with lock:
            keys = list(TRANSACTIONS_TO_SEND.keys())

            for transaction_id in keys:
                if (
                    transaction_id in TRANSACTIONS_TO_SEND
                    and TRANSACTIONS_TO_SEND[transaction_id]["state"] == "IN_PROGRESS"
                    and time.time() - TRANSACTIONS_TO_SEND[transaction_id]["claimed_at"]
                    > DOG_TIMER
                ):
                    # IN_PROGRESS transaction is stuck
                    # Resubmit with higher gas fees
                    # This should trigger a resend with higher fees, not a put back into pending state
                    # Putting back in pending will assign it to a new nonce
                    # TODO: make a helper that immediately resubmits with higher gas
                    print(
                        f"Transaction {transaction_id} stuck. Placing back in PENDING state."
                    )
                    TRANSACTIONS_TO_SEND[transaction_id]["state"] = "PENDING"

        await asyncio.sleep(DOG_TIMER)


async def main():
    global lock
    lock = asyncio.Lock()

    start_http_server(PROMETHEUS_PORT)
    # implement critical error handling here, need nonce to succeed
    await get_wallet_nonce()
    await asyncio.gather(
        poll_for_transactions(), send_transactions_to_poly(), the_watcher_doggenstein()
    )

    # poll_thread = threading.Thread(target=poll_for_transactions)
    # poll_thread.start()

    # send_thread = threading.Thread(target=send_transactions_to_poly)
    # send_thread.start()

    # Wait for threads to complete before the main program exits
    # poll_thread.join()
    # send_thread.join()

    print("Main thread finished.")
    return


if __name__ == "__main__":
    asyncio.run(main())
