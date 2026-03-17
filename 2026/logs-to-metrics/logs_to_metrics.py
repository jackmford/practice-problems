import json
import logging
import sys
import time

from collections import defaultdict
from datetime import datetime, timedelta, timezone

logger = logging.getLogger(__name__)

endpoint_latency = defaultdict(list)
now = None


def calculate_summaries():
    if now is not None:
        to_end = now
    else:
        raise Exception("No log lines have been processed")

    start = datetime.now(timezone.utc)

    avgs = []
    while start > to_end:
        time_range_end = start
        time_range_start = start - timedelta(seconds=10)
        for endpoint, data in endpoint_latency.items():
            avg = 0
            ctr = 0
            for d in data:
                log_time = datetime.fromisoformat(d["timestamp"].replace("Z", "+00:00"))
                if log_time > time_range_start and log_time < time_range_end:
                    avg += d.get("latency_ms")
                    ctr += 1
            avg = avg / ctr
            avgs.append([endpoint, avg])

        print(f"From {time_range_start} to {time_range_end}: ")
        for res in avgs:
            print(f"{res[0]} | Avg Latency: {res[1]}")

        start = start - timedelta(seconds=10)


def process_log_lines():
    global now
    now = datetime.now(timezone.utc)
    # 1. Read file (line by line)
    for line in sys.stdin:
        try:
            data = json.loads(line)
            endpoint = data.get("endpoint")
            endpoint_latency[endpoint].append(
                {
                    "timestamp": data.get("timestamp"),
                    "latency_ms": data.get("latency_ms"),
                    "status": data.get("status"),
                }
            )

        except json.JSONDecodeError as e:
            logger.error(f"Failed parse line as json: {str(e)}")


def main():
    # Scenario: You have a high-volume service producing JSON logs. You need to write a utility
    # that reads these logs from stdin,
    # calculates the average latency per "endpoint" over a 10-second window, and prints a summary.

    # Constraint: The solution must be memory-efficient (don't load the whole file) and handle malformed JSON gracefully.

    # Bonus: Implement a context.Context to handle graceful shutdowns (SIGINT/SIGTERM).

    process_log_lines()
    calculate_summaries()

    # 2. Process
    # 3. Print summary


if __name__ == "__main__":
    main()
