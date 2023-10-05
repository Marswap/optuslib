from pydantic import BaseModel


class OracleJetton(BaseModel):
    address: str
    name: str
    image: str | None
    symbol: str
    decimals: int
    existing_pair_jettons: list[str] = []
