import json
import time

from redis import Redis
from rq import Queue

REDIS_CONN = Redis(host="redis", port=6379)
queue = Queue(connection=REDIS_CONN)
QUEUE_NAME = 'QUEUE'
RUN_TIME = 4

def poll_for_transactions():
    item = REDIS_CONN.rpop(QUEUE_NAME)
    if item:
        print("Pulling transaction from queue")
        print(json.loads(item.decode('utf-8')))
    return


def main():
    print("hi")
    while True:
        poll_for_transactions()
        time.sleep(RUN_TIME)
    return


if __name__ == "__main__":
    print("hi")
    main()

print("hi2")

