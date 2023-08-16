from pydantic import BaseModel

from .indicators import Indicator, UsdAmount


class OperationToken(BaseModel):
    symbol: str
    amount: Indicator = Indicator()


class OperationUserAccount(BaseModel):
    id: int
    address: str


class DashboardBaseOperation(BaseModel):
    id: int
    timestamp: int
    name: str | None
    user_account: OperationUserAccount | None
    type: str | None
    amount: UsdAmount | None
    token_0: OperationToken | None
    token_1: OperationToken | None
    time_ago: str | None


class DashboardOperation(DashboardBaseOperation):
    pass
