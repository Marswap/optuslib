from pydantic import BaseModel

from .dex import DashboardBaseDex
from .token import DashboardBaseToken
from .pair import DashboardBasePair


class DashboardSearch(BaseModel):
    dex_list: list[DashboardBaseDex] = []
    token_list: list[DashboardBaseToken] = []
    pair_list: list[DashboardBasePair] = []
