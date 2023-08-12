from pydantic import BaseModel

from .charts import ChartPoint
from .indicators import PriceIndicator, Indicator, FeeIndicator


class DashboardDexOverview(BaseModel):
    ton_price: PriceIndicator = PriceIndicator()
    transactions_24h: Indicator = Indicator()
    pairs_number: Indicator = Indicator()
    fees_24h: FeeIndicator = FeeIndicator()
    liquidity_chart: list[ChartPoint] = []
    volume_chart: list[ChartPoint] = []
