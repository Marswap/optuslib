from pydantic import BaseModel

from .charts import ChartPoint, CandleChartPoint
from .indicators import LiquidityIndicator, UsdLiquidityIndicator, UsdVolumeIndicator, PriceIndicator, Indicator


class DashboardBaseToken(BaseModel):
    address: str
    symbol: str
    name: str
    icon: str
    decimals: int
    native_liquidity: LiquidityIndicator = LiquidityIndicator()
    liquidity: UsdLiquidityIndicator = UsdLiquidityIndicator()
    volume_24h: UsdVolumeIndicator = UsdVolumeIndicator()
    current_usd_price: PriceIndicator = PriceIndicator()
    transactions_24h: Indicator = Indicator()


class DashboardToken(DashboardBaseToken):
    liquidity_graph: list[ChartPoint] = []
    volume_graph: list[ChartPoint] = []
    usd_price_graph: list[CandleChartPoint] = []


class DashboardExtendedToken(DashboardToken):
    id: int | None
    start_time: int | None
    usd_price: dict[int, float] = {}
    is_usd_price_updated: bool | None
    liquidity_change: dict[int, int] = {}
    token_liquidity: dict[int, int] = {}
    token_volume: dict[int, int] = {}
    token_transactions: dict[int, int] = {}
    usd_liquidity: dict[int, float] = {}
    usd_volume: dict[int, float] = {}
