from pydantic import BaseModel, root_validator

from ...func.ton import to_friendly_address, to_raw_address


class BaseUserFriendlyAddressModel(BaseModel):
    pass

    @root_validator
    def convert_addresses(cls, values: dict) -> dict:
        for key in (
            "minter_address",
            "pool_address",
            "deployer_address",
            "address",
            "router_address",
            "user_address",
            "from_address",
            "to_address",
            "from_jetton_wallet_address",
        ):
            if key in values.keys() and values[key] and ":" in values[key]:
                values[key] = to_friendly_address(values[key])
        return values


class BaseRawAddressModel(BaseModel):
    pass

    @root_validator
    def convert_addresses(cls, values: dict) -> dict:
        for key in (
            "minter_address",
            "pool_address",
            "deployer_address",
            "address",
            "router_address",
            "user_address",
            "from_address",
            "to_address",
            "from_jetton_wallet_address",
        ):
            if key in values.keys() and values[key]:
                values[key] = to_raw_address(values[key])
        return values
