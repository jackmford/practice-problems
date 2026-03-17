import json
import time
import random
import sys
from datetime import datetime

endpoints = ["/api/v1/user", "/api/v1/order", "/api/v1/inventory", "/health"]
levels = ["info", "info", "info", "warn", "error"]


def generate_log():
    # Randomly introduce a malformed line 5% of the time
    if random.random() < 0.05:
        return "!!! MALFORMED LOG LINE !!!"

    log = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "endpoint": random.choice(endpoints),
        "latency_ms": round(
            random.uniform(10.0, 500.0)
            if random.random() > 0.1
            else random.uniform(500.0, 2000.0),
            2,
        ),
        "status": random.choice([200, 200, 200, 201, 404, 500]),
        "level": random.choice(levels),
    }
    return json.dumps(log)


if __name__ == "__main__":
    try:
        while True:
            print(generate_log())
            sys.stdout.flush()
            # Adjust sleep to simulate different traffic speeds
            time.sleep(0.01)
    except KeyboardInterrupt:
        pass
