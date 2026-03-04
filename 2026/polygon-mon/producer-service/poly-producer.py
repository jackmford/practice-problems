import json
import random
import time
import uuid

from prometheus_client import start_http_server, Gauge, Info
from redis import Redis
from rq import Queue

REDIS_CONN = Redis(host="redis", port=6379)

# Using a queue here but for multiple consumers could use
# Redis STREAM instead
queue = Queue(connection=REDIS_CONN)
QUEUE_NAME = 'QUEUE'
RUN_TIME = 5
PROMETHEUS_PORT = 8005

QUEUE_DEPTH = Gauge('transaction_queue_depth', 'Current depth of the Redis queue holding transactions')

# Make func to randomly push onto redis queue
# This simulates MATCHED transactions coming from the DB ready to be
# Sent to Polygon chain
def push_transaction():

    print(REDIS_CONN.llen(QUEUE_NAME))
    QUEUE_DEPTH.set(REDIS_CONN.llen(QUEUE_NAME))
    # Push something half the time
    data = {
        "transaction_id": str(uuid.uuid4),
        "maker_id":  str(uuid.uuid4),
        "taker_id":  str(uuid.uuid4),
        "state": "MATCHED",
    }
    if random.random() < 0.5:
        print("Pushing transaction to queue")
        REDIS_CONN.rpush(QUEUE_NAME, json.dumps(data))

def main():
    start_http_server(PROMETHEUS_PORT)
    print("hi")
    while True:
        push_transaction()
        time.sleep(RUN_TIME)
    return

if __name__ == "__main__":
    main()
