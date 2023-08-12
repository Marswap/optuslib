from pydantic import BaseModel


from .charts import ChartPoint
from .indicators import PriceIndicator, Indicator, FeeIndicator


class BlockchainCharts(BaseModel):
    transactions_chart: list[ChartPoint] = []
    dau_chart: list[ChartPoint] = []
    new_accounts_chart: list[ChartPoint] = []
    accounts_chart: list[ChartPoint] = []


class BlockchainOverview(BaseModel):
    type: str = "blockchain"
    service: BlockchainCharts = BlockchainCharts()
    user: BlockchainCharts = BlockchainCharts()
    total: BlockchainCharts = BlockchainCharts()

    def del_last_values(self) -> None:
        for field_name in self.get_fields(without_fields=["type"]):
            field = getattr(self, field_name)
            for chart_name in field.get_fields(without_fields=[]):
                chart = getattr(field, chart_name)
                chart.pop()
                setattr(field, chart_name, chart)
            setattr(self, field_name, field)


class DashboardOverview(BaseModel):
    ton_price: PriceIndicator = PriceIndicator()
    transactions_24h: Indicator = Indicator()
    pairs_number: Indicator = Indicator()
    fees_24h: FeeIndicator = FeeIndicator()
    liquidity_graph: list[ChartPoint] = []
    volume_graph: list[ChartPoint] = []

    class Config:
        use_enum_values = True


class Overview(DashboardOverview):
    start_time: int | None
    usd_liquidity: dict[int, float] = {}
    usd_volume: dict[int, float] = {}


class DashboardDexOverview(BaseModel):
    ton_price: PriceIndicator = PriceIndicator()
    transactions_24h: Indicator = Indicator()
    pairs_number: Indicator = Indicator()
    fees_24h: FeeIndicator = FeeIndicator()
    liquidity_chart: list[ChartPoint] = []
    volume_chart: list[ChartPoint] = []
