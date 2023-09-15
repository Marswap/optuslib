from pydantic import BaseModel

from .account import DashboardBaseAccount, DashboardAccount
from .dex import DashboardBaseDex, DashboardDex
from .token import DashboardBaseToken, DashboardToken
from .pair import DashboardBasePair, DashboardPair


class DashboardSearch(BaseModel):
    dex: DashboardDex | None
    token: DashboardToken | None
    pair: DashboardPair | None
    account: DashboardAccount | None
    dex_list: list[DashboardBaseDex] = []
    token_list: list[DashboardBaseToken] = []
    pair_list: list[DashboardBasePair] = []
    account_list: list[DashboardBaseAccount] = []
