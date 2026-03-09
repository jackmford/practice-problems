import json
import asyncio
import random
import time
import heapq

from redis import Redis
from rq import Queue
from prometheus_client import start_http_server, Counter, Histogram

lock = asyncio.Lock()

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
    buckets=[0.05, 0.1, 0.25, 0.5, 1.0, 2.5, 5.0, 10.0],
)

TRANSACTION_MAX_RETRIES = 3
RETRY_BASE_DELAY = 0.25
DOG_TIMER = 60


async def poll_for_transactions():
    while True:
        item = REDIS_CONN.rpop(QUEUE_NAME)
        if item:
            print("Pulling transaction from queue")
            try:
                item_json = json.loads(item)  # type:ignore
                async with lock:
                    TRANSACTIONS_TO_SEND[item_json["transaction_id"]] = item_json
                    TRANSACTIONS_TO_SEND[item_json["transaction_id"]]["state"] = (
                        "PENDING"
                    )
                    TRANSACTIONS_TO_SEND[item_json["transaction_id"]]["claimed_at"] = (
                        time.time()
                    )

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
    print(f"Sending {transaction_id} to Poly...")
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
                        print(f"{transaction_id} accepted on attempt {attempt + 1}.")
                        ACCEPTED_TRANSACTIONS.inc()
                        del TRANSACTIONS_TO_SEND[transaction_id]
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
                    print(
                        f"Transaction {transaction_id} stuck. Placing back in PENDING state."
                    )
                    TRANSACTIONS_TO_SEND[transaction_id]["state"] = "PENDING"

        await asyncio.sleep(DOG_TIMER)


async def main():
    start_http_server(PROMETHEUS_PORT)
    await asyncio.gather(poll_for_transactions(), send_transactions_to_poly())

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
