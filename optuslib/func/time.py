from datetime import datetime, timezone


DELTA_24H = 24 * 60 * 60


def get_now_timestamp() -> int:
    return int(datetime.now(timezone.utc).timestamp())
