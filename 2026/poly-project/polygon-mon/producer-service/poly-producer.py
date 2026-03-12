import json
import structlog
import random
import time
import uuid

from prometheus_client import start_http_server, Gauge, Info
from redis import Redis
from rq import Queue

structlog.configure(
    processors=[
        structlog.processors.add_log_level,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.JSONRenderer(),
    ]
)

logger = structlog.get_logger()


REDIS_CONN = Redis(host="redis", port=6379)

# Using a queue here but for multiple consumers could use
# Redis STREAM instead
queue = Queue(connection=REDIS_CONN)
QUEUE_NAME = "QUEUE"
RUN_TIME = 5
PROMETHEUS_PORT = 8005

QUEUE_DEPTH = Gauge(
    "transaction_queue_depth", "Current depth of the Redis queue holding transactions"
)


# Make func to randomly push onto redis queue
# This simulates MATCHED transactions coming from the DB ready to be
# Sent to Polygon chain
def push_transaction():

    data = {
        "transaction_id": str(uuid.uuid4()),
        "maker_id": str(uuid.uuid4()),
        "taker_id": str(uuid.uuid4()),
        "state": "MATCHED",
    }
    logger.bind(
        transaction_id=data["transaction_id"],
        maker_id=data["maker_id"],
        taker_id=data["taker_id"],
        state=data["state"],
    )

    logger.info("current_queue_len", queue_len=REDIS_CONN.llen(QUEUE_NAME))
    QUEUE_DEPTH.set(REDIS_CONN.llen(QUEUE_NAME))  # type:ignore
    # Push something half the time
    if random.random() < 0.5:
        # print("Pushing transaction to queue")
        logger.debug("transaction_push")
        REDIS_CONN.rpush(QUEUE_NAME, json.dumps(data))


def main():
    start_http_server(PROMETHEUS_PORT)
    while True:
        push_transaction()
        time.sleep(RUN_TIME)
    return


if __name__ == "__main__":
    main()
