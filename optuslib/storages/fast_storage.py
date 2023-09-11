from ..schemas import (
    DashboardDexOverview,
    DashboardDex,
    DashboardBaseDex,
    DashboardExtendedDex,
    DashboardToken,
    DashboardBaseToken,
    DashboardExtendedToken,
    DashboardPair,
    DashboardBasePair,
    DashboardAccount,
    DashboardBaseAccount,
    Pool,
)


class FastStorage:
    async def close(self) -> None:
        ...

    async def set_price(self, key: str, price: dict[int, float]) -> None:
        ...

    async def get_price(self, key: str) -> dict[int, float] | None:
        ...

    async def set_ton_usd_price(self, price: dict[int, float]) -> None:
        ...

    async def get_ton_usd_price(self) -> dict[int, float] | None:
        ...

    async def set_dashboard_dex_overview(self, dashboard_dex_overview: DashboardDexOverview) -> None:
        ...

    async def get_dashboard_dex_overview(self) -> DashboardDexOverview | None:
        ...

    async def set_dashboard_dex(self, dashboard_dex: DashboardExtendedDex) -> None:
        ...

    async def get_dashboard_dex(
        self,
        dex_id: int,
        is_extended: bool = False,
    ) -> DashboardDex | DashboardExtendedDex | None:
        ...

    async def set_dashboard_token(self, dashboard_token: DashboardExtendedToken, dex_id: int | None) -> None:
        ...

    async def get_dashboard_token(
        self,
        token_id: int,
        dex_id: int | None,
        is_extended: bool = False,
    ) -> DashboardToken | DashboardExtendedToken | None:
        ...

    async def set_dashboard_pair(self, dashboard_pair: DashboardPair, dex_id: int | None) -> None:
        ...

    async def get_dashboard_pair(self, pair_id: int, dex_id: int | None) -> DashboardPair | None:
        ...

    async def set_dashboard_account(self, dashboard_account: DashboardAccount) -> None:
        ...

    async def get_dashboard_account(self, account_id: int) -> DashboardAccount | None:
        ...

    async def set_dashboard_dex_list(self, dex_list: list[DashboardBaseDex]) -> None:
        ...

    async def get_dashboard_dex_list(self) -> list[DashboardBaseDex] | None:
        ...

    async def set_dashboard_token_list(self, token_list: list[DashboardBaseToken], dex_id: int | None) -> None:
        ...

    async def get_dashboard_token_list(self, dex_id: int | None) -> list[DashboardBaseToken] | None:
        ...

    async def set_dashboard_pair_list(self, pair_list: list[DashboardBasePair], dex_id: int | None) -> None:
        ...

    async def get_dashboard_pair_list(self, dex_id: int | None) -> list[DashboardBasePair] | None:
        ...

    async def set_dashboard_account_list(self, account_list: list[DashboardBaseAccount], dex_id: int | None) -> None:
        ...

    async def get_dashboard_account_list(self, dex_id: int | None) -> list[DashboardBaseAccount] | None:
        ...

    async def set_pool_list(self, pool_list: list[Pool]) -> None:
        ...

    async def get_pool_list(self) -> list[Pool] | None:
        ...
