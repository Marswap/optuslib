from pydantic import BaseModel


from .charts import ChartPoint, CandleChartPoint, PairSequence
from .indicators import (
    PriceIndicator,
    LiquidityIndicator,
    UsdLiquidityIndicator,
    UsdVolumeIndicator,
    FeeIndicator,
    AprIndicator,
)
from .token import DashboardBaseToken


class TokenIndicators(BaseModel):
    current_pair_price: PriceIndicator = PriceIndicator()
    pool_quantity: LiquidityIndicator = LiquidityIndicator()
    current_usd_price: PriceIndicator = PriceIndicator()


class DashboardBasePair(BaseModel):
    id: int | None
    address: str
    name: str
    token_one: DashboardBaseToken | None
    token_two: DashboardBaseToken | None
    liquidity: UsdLiquidityIndicator = UsdLiquidityIndicator()
    volume_24h: UsdVolumeIndicator = UsdVolumeIndicator()
    volume_7d: UsdVolumeIndicator = UsdVolumeIndicator()
    fees_24h: FeeIndicator = FeeIndicator()
    fees_liquidity_ratio: AprIndicator = AprIndicator()
    symbol_one_indicators: TokenIndicators = TokenIndicators()
    symbol_two_indicators: TokenIndicators = TokenIndicators()


class DashboardPair(DashboardBasePair):
    liquidity_graph: list[ChartPoint] = []
    volume_graph: list[ChartPoint] = []
    symbol_one_price_graph: list[CandleChartPoint] = []
    symbol_two_price_graph: list[CandleChartPoint] = []


class DashboardExtendedPair(DashboardPair):
    start_time: int | None
    liquidity_change: PairSequence = PairSequence()
    liquidity_seq: PairSequence = PairSequence()
    volume_sec: PairSequence = PairSequence()
    token_one_liquidity_change: dict[int, int] = {}
    token_two_liquidity_change: dict[int, int] = {}
    token_one_liquidity: dict[int, int] = {}
    token_two_liquidity: dict[int, int] = {}
    token_one_volume: dict[int, int] = {}
    token_two_volume: dict[int, int] = {}
    token_one_pair_price: dict[int, float] = {}
    token_two_pair_price: dict[int, float] = {}
    usd_liquidity: dict[int, float] = {}
    usd_volume: dict[int, float] = {}
