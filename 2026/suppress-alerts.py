# You receive alert events from monitoring:
#
# alerts = [
#    {"service": "api", "alert": "HighLatency", "timestamp": 100},
#    {"service": "api", "alert": "HighLatency", "timestamp": 120},
#    {"service": "api", "alert": "HighLatency", "timestamp": 170},
#    {"service": "db", "alert": "CPUHigh", "timestamp": 180},
#    {"service": "api", "alert": "ErrorRate", "timestamp": 190},
# ]
#
# Write:
#
# def suppress_alerts(alerts: list[dict], suppression_window: int) -> list[dict]:
# Requirements
#
# Return a list of alerts after suppressing repeats.
#
# An alert should be suppressed if another alert with the same service and alert has already been emitted within the last suppression_window seconds.
#
# For example:
#
# suppress_alerts(alerts, 60)
#
# should return:
#
# [
#    {"service": "api", "alert": "HighLatency", "timestamp": 100},
#    {"service": "api", "alert": "HighLatency", "timestamp": 170},
#    {"service": "db", "alert": "CPUHigh", "timestamp": 180},
#    {"service": "api", "alert": "ErrorRate", "timestamp": 190},
# ]
#
# Because the alert at timestamp 120 is only 20 seconds after the emitted HighLatency alert at 100, so it is suppressed. The alert at 170 is 70 seconds after 100, so it is emitted.

# Rules
# Input may be out of order.
# Return emitted alerts ordered by timestamp.
# Suppression is based on the last emitted alert, not the last seen alert.
# Alerts for different services should not suppress each other.
# Different alert names for the same service should not suppress each other.
# Ignore alerts missing service, alert, or timestamp.
# Do not modify the input list.
# Aim for O(n log n) time due to sorting.


def suppress_alerts(alerts: list[dict], suppression_window: int) -> list[dict]:

    latest_alerts = {}
    emit_alerts = []

    for alert in alerts:
        service = alert.get("service")
        alert_name = alert.get("alert")
        timestamp = alert.get("timestamp")

        if service is None or alert_name is None or timestamp is None:
            continue

        current_alert = latest_alerts.get((service, alert_name))
        if current_alert is None:
            latest_alerts[(service, alert_name)] = timestamp
            emit_alerts.append(alert)
            continue

        suppression_time = current_alert + suppression_window

        if timestamp <= suppression_time:
            continue

        latest_alerts[(service, alert_name)] = timestamp
        emit_alerts.append(alert)

    return emit_alerts


def main():
    alerts = [
        {"service": "api", "alert": "HighLatency", "timestamp": 100},
        {"service": "api", "alert": "HighLatency", "timestamp": 120},
        {"service": "api", "alert": "HighLatency", "timestamp": 170},
        {"service": "db", "alert": "CPUHigh", "timestamp": 180},
        {"service": "api", "alert": "ErrorRate", "timestamp": 190},
    ]
    # pre process step
    # sort the incoming alerts for suppress algorithm
    sorted_alerts = sorted(alerts, key=lambda item: item["timestamp"])

    print(suppress_alerts(sorted_alerts, 60))


if __name__ == "__main__":
    main()
