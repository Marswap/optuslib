from pydantic import BaseModel

from .contract import Contract


class Dex(BaseModel):
    id: int | None
    name: str
    description: str | None
    router_contract: Contract | None

    class Config:
        orm_mode = True
