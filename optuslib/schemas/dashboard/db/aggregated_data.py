from pydantic import BaseModel

from .dex import Dex
from .pair import Pair
from .contract import Contract
from ..account import DashboardAccount


class Data(BaseModel):
    account: DashboardAccount | None


class AggregatedData(BaseModel):
    id: int | None
    dex: Dex | None
    pair: Pair | None
    token_contract: Contract | None
    user_contract: Contract | None
    data: Data = Data()
