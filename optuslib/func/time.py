from datetime import datetime, timezone


DELTA_24H = 24 * 60 * 60


def now_timestamp() -> int:
    return int(datetime.now(timezone.utc).timestamp())


def timestamp_point(timestamp: int, time_interval: int) -> int:
    return timestamp // time_interval * time_interval
