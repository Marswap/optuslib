import datetime
from pydantic import BaseModel


class PricePointData(BaseModel):
    v: list[float]
    c: list[float] | None


class Data(BaseModel):
    points: dict[int, PricePointData]


class Status(BaseModel):
    timestamp: datetime.datetime
    error_code: str
    error_message: str
    elapsed: str
    credit_count: int


class Price(BaseModel):
    data: Data
    status: Status
