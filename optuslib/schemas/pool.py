from pydantic import BaseModel

from .contract import Contract
from .pair import Pair
from .dex import Dex


class Pool(BaseModel):
    id: int | None
    contract: Contract
    dex: Dex | None
    pair: Pair

    class Config:
        orm_mode = True
