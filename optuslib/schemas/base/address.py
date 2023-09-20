from pydantic import BaseModel, root_validator

from ...func.ton import to_raw_address, to_friendly_address


class Address(BaseModel):
    raw: str | None
    user_friendly: str | None

    @root_validator
    def validate_addresses(cls, values: dict) -> dict:
        raw_address = values.get("raw", None)
        user_friendly_address = values.get("user_friendly", None)

        if raw_address and not user_friendly_address:
            values["user_friendly"] = to_friendly_address(raw_address)

        if user_friendly_address and not raw_address:
            values["raw"] = to_raw_address(user_friendly_address)

        return values
