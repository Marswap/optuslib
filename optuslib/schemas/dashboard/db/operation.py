from pydantic import BaseModel

from .operation_type import OperationType
from .contract import Contract
from .pool import Pool


class Operation(BaseModel):
    id: int | None
    timestamp: int
    operation_type: OperationType | None
    user_contract: Contract | None
    pool: Pool | None
    token_0_amount: int
    token_1_amount: int
    token_lp_amount: int
    transaction_count: int

    class Config:
        orm_mode = True
