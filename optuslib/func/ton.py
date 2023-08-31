from pytonlib.utils.address import detect_address


def to_friendly_address(address: str) -> str | None:
    try:
        return detect_address(address)["bounceable"]["b64url"]

    except Exception:
        return None


def to_raw_address(address: str) -> str | None:
    try:
        return detect_address(address)["raw_form"]

    except Exception:
        return None
