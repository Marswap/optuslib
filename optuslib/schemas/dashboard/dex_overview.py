from pydantic import BaseModel

from .charts import Chart
from .indicators import PriceIndicator, Indicator, FeeIndicator


class DashboardDexOverview(BaseModel):
    ton_price: PriceIndicator = PriceIndicator()
    swaps_24h: Indicator = Indicator()
    pairs_number: Indicator = Indicator()
    fees_24h: FeeIndicator = FeeIndicator()
    liquidity_chart: Chart = Chart()
    volume_chart: Chart = Chart()
