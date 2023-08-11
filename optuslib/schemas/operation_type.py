from pydantic import BaseModel


class OperationType(BaseModel):
    id: int | None
    name: str
    description: str | None

    class Config:
        orm_mode = True
