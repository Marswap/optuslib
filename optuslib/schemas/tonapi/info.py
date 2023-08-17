from pydantic import BaseModel


# https://tonapi.io/v1/jetton/getInfo


class JettonMetadata(BaseModel):
    address: str
    catalogs: list[str] | None
    decimals: int
    description: str | None
    image: str | None
    name: str
    social: list[str] | None
    symbol: str
    websites: list[str] | None


class JettonInfo(BaseModel):
    metadata: JettonMetadata
    mintable: bool
    total_supply: str
    verification: str
    verification: str
