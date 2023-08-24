from pydantic import BaseModel

from .charts import Chart
from .indicators import Indicator, UsdLiquidity, UsdVolume
from .pair import DashboardExtendedPair


class DashboardBaseAccount(BaseModel):
    id: int | None
    address: str
    name: str | None
    description: str | None
    liquidity: UsdLiquidity = UsdLiquidity()
    volume_24h: UsdVolume = UsdVolume()
    transactions_24h: Indicator = Indicator()


class DashboardAccount(DashboardBaseAccount):
    liquidity_chart: Chart = Chart()
    volume_chart: Chart = Chart()


class DashboardExtendedAccount(DashboardAccount):
    start_time: int | None
    pool_data: dict[int, DashboardExtendedPair]
