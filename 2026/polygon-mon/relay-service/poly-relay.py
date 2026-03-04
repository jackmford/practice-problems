import json
import time
import threading
import random

from redis import Redis
from rq import Queue
from prometheus_client import start_http_server, Counter

REDIS_CONN = Redis(host="redis", port=6379)

# Using a queue here but for multiple consumers could use
# Redis STREAM instead
queue = Queue(connection=REDIS_CONN)
QUEUE_NAME = 'QUEUE'
POLL_TIME = 10
SEND_TIME = 15
PROMETHEUS_PORT = 8006

TRANSACTIONS_TO_SEND = {}

FAILED_TRANSACTIONS = Counter('failed_poly_transactions', 'Counter for transactions that are reported failed from Poly')
ACCEPTED_TRANSACTIONS = Counter('accepted_poly_transactions', 'Counter for transactions that are reported accepted from Poly')

def poll_for_transactions():
    while True:
        item = REDIS_CONN.rpop(QUEUE_NAME)
        if item:
            print("Pulling transaction from queue")
            try:
                item_json = json.loads(item.decode('utf-8'))
                TRANSACTIONS_TO_SEND[item_json["transaction_id"]] = item_json

            except Exception as e:
                print(f"Exception processing item {item.decode('utf-8')}")
            
        time.sleep(POLL_TIME)
    return

# Mock API
def poly_request():
    if random.random() < 0.1:
        return 500

    return 200

def send_transactions_to_poly():
    while True:
        for transaction_id in list(TRANSACTIONS_TO_SEND.keys()):
            response = poly_request()

            if response == 200:
                # Transaction is "ACCEPTED", but not "FINALIZED" yet
                # Indexer service handles watching for FINALIZED and
                # Updating DB
                ACCEPTED_TRANSACTIONS.inc()
                del TRANSACTIONS_TO_SEND[transaction_id]
            else:
                FAILED_TRANSACTIONS.inc()
                print(f"{transaction_id} failed. Resubmitting.")
                

        time.sleep(SEND_TIME)
    return



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

