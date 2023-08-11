from pydantic import BaseModel


class ContractMetadata(BaseModel):
    id: int | None
    name: str = "Unknown jetton"
    description: str | None
    image: str | None
    symbol: str = "UNKNOWN"
    decimals: int = 9

    class Config:
        orm_mode = True
