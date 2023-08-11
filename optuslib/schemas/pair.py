from pydantic import BaseModel

from .contract import Contract


class Pair(BaseModel):
    id: int | None
    name: str
    token_0_contract: Contract
    token_1_contract: Contract

    class Config:
        orm_mode = True
