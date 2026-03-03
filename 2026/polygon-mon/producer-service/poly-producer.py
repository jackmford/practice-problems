import json
import random
import time
import uuid

from redis import Redis
from rq import Queue

REDIS_CONN = Redis(host="redis", port=6379)
queue = Queue(connection=REDIS_CONN)
QUEUE_NAME = 'QUEUE'
RUN_TIME = 5

# Make func to randomly push onto redis queue
# This simulates MATCHED transactions coming from the DB ready to be
# Sent to Polygon chain

def push_transaction():
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
    print("hi")
    while True:
        push_transaction()
        time.sleep(RUN_TIME)
    return

if __name__ == "__main__":
    main()
