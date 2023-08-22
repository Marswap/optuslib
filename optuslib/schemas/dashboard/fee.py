from pydantic import BaseModel

from .charts import Chart


class DashboardFeeChart(BaseModel):
    daily: Chart = Chart()
    cumulative: Chart = Chart()
