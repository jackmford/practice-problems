import json
import time
import threading
import random

from redis import Redis
from rq import Queue
from prometheus_client import start_http_server, Counter, Histogram

lock = threading.Lock()

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


def poll_for_transactions():
    while True:
        item = REDIS_CONN.rpop(QUEUE_NAME)
        if item:
            print("Pulling transaction from queue")
            try:
                item_json = json.loads(item)  # type:ignore
                with lock:
                    TRANSACTIONS_TO_SEND[item_json["transaction_id"]] = item_json

            except Exception as e:
                print(f"Exception processing item {item.decode('utf-8')}: {e}")  # type:ignore

        time.sleep(POLL_TIME)


# Mock API
def poly_request():
    if random.random() < 0.1:
        return 500

    return 200


def send_transactions_to_poly():
    while True:
        with lock:
            # These keys should all be marked as IN PROGRESS so no other threads pick them up
            # Could use a temporary function scoped dict, copy them over, remove them from main, submit failed ones back onto main dict
            keys = list(TRANSACTIONS_TO_SEND.keys())

        for transaction_id in keys:
            with REQUEST_DURATION.time():
                response = poly_request()

            if response == 200:
                # Transaction is "ACCEPTED", but not "FINALIZED" yet
                # Indexer service handles watching for FINALIZED and
                # Updating DB
                print(f"{transaction_id} accepted.")
                ACCEPTED_TRANSACTIONS.inc()
                with lock:
                    if transaction_id in TRANSACTIONS_TO_SEND:
                        del TRANSACTIONS_TO_SEND[transaction_id]
            else:
                FAILED_TRANSACTIONS.inc()
                if (
                    "retries" in TRANSACTIONS_TO_SEND[transaction_id]
                    and TRANSACTIONS_TO_SEND[transaction_id]["retries"] >= 3
                ):
                    print(
                        f"{transaction_id} failed. Retries exceeded. Marking as failed in DB."
                    )
                    # Mark as failed in DB MOCK

                print(f"{transaction_id} failed. Retrying.")
                TRANSACTIONS_TO_SEND[transaction_id].setdefault("retries", 0)
                TRANSACTIONS_TO_SEND[transaction_id]["retries"] += 1

        time.sleep(SEND_TIME)


def main():
    start_http_server(PROMETHEUS_PORT)
    print("hi")
    poll_thread = threading.Thread(target=poll_for_transactions)
    poll_thread.start()

    send_thread = threading.Thread(target=send_transactions_to_poly)
    send_thread.start()

    # Wait for threads to complete before the main program exits
    poll_thread.join()
    send_thread.join()

    print("Main thread finished.")
    return


if __name__ == "__main__":
    main()
