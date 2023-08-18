from pydantic import BaseModel

from ...tonapi.annotated_trace import Trace
from .contract import Contract
from .dex import Dex


class DexTrace(BaseModel):
    id: int | None
    hash: str
    dex: Dex | None
    contract: Contract
    timestamp: int
    lt: int
    data: Trace
    is_parsed: bool | None

    class Config:
        orm_mode = True
