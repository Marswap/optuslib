from pydantic import BaseModel, root_validator

from .meta import DashboardMeta
from ...func.ton import to_friendly_address


class DashboardBase(BaseModel):
    id: int | None
    address: str
    user_friendly_address: str | None

    @root_validator(pre=True)
    def convert_address(cls, values: dict) -> dict:
        if values.get("user_friendly_address") is None:
            values["user_friendly_address"] = to_friendly_address(values["address"])

        return values


class DashboardBaseList(BaseModel):
    meta: DashboardMeta
