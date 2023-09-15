from pydantic import BaseModel

from .account import DashboardBaseAccount
from .dex import DashboardBaseDex
from .token import DashboardBaseToken
from .pair import DashboardBasePair


class DashboardSearch(BaseModel):
    account_list: list[DashboardBaseAccount] = []
    dex_list: list[DashboardBaseDex] = []
    token_list: list[DashboardBaseToken] = []
    pair_list: list[DashboardBasePair] = []
