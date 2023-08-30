from .db.dex import Dex
from .charts import Chart
from .indicators import Indicator, UsdLiquidity, UsdVolume, PriceIndicator, FeeIndicator


class DashboardBaseDex(Dex):
    liquidity: UsdLiquidity = UsdLiquidity()
    volume_24h: UsdVolume = UsdVolume()
    swaps_24h: Indicator = Indicator()
    pairs_number: Indicator = Indicator()


class DashboardDex(DashboardBaseDex):
    ton_price: PriceIndicator = PriceIndicator()
    fees_24h: FeeIndicator = FeeIndicator()
    liquidity_chart: Chart = Chart()
    volume_chart: Chart = Chart()


class DashboardExtendedDex(DashboardDex):
    start_time: int | None
    usd_liquidity: dict[int, float] = {}
    usd_volume: dict[int, float] = {}
    ton_liquidity: dict[int, float] = {}
    ton_volume: dict[int, float] = {}
