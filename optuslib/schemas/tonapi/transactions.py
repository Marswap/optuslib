from pydantic import BaseModel, validator

from .annotated_trace import AnnotationData


# https://tonapi.io/v1/blockchain/getTransactions


class TonapiTransaction(BaseModel):
    hash: str
    account: str
    lt: int
    utime: int

    @validator("account", pre=True)
    def get_account_address(cls, value):
        return value["address"]


class TonapiTransactionList(BaseModel):
    transactions: list[TonapiTransaction] | None


class TonapiTransactionAccount(BaseModel):
    account: str
    utime: int


class ParsedAnnotationData(BaseModel):
    type: str
    data: AnnotationData
