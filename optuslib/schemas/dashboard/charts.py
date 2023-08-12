from pydantic import BaseModel


class ChartPoint(BaseModel):
    timestamp: int | None
    time: str | None
    value: float | None


class CandleChartPoint(BaseModel):
    timestamp: int | None
    time: str | None
    open: float | None
    close: float | None
    high: float | None
    low: float | None


class Chart(BaseModel):
    ton: list[ChartPoint] = []
    usd: list[ChartPoint] = []
