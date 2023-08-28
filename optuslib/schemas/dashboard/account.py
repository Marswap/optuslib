from pydantic import BaseModel

from .charts import Chart, ChartPoint
from .indicators import Indicator, UsdLiquidity, UsdVolume


class DashboardBaseAccount(BaseModel):
    id: int | None
    address: str
    name: str | None
    description: str | None
    liquidity: UsdLiquidity = UsdLiquidity()
    volume_total: UsdVolume = UsdVolume()
    volume_24h: UsdVolume = UsdVolume()
    swaps_total: Indicator = Indicator()
    swaps_24h: Indicator = Indicator()


class DashboardAccount(DashboardBaseAccount):
    liquidity_chart: Chart = Chart()
    volume_chart: Chart = Chart()
    swaps_chart: list[ChartPoint] = []
