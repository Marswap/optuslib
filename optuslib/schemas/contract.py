from pydantic import BaseModel, root_validator

from .contract_metadata import ContractMetadata


class Contract(BaseModel):
    id: int | None
    address: str
    workchain_id: int
    account_id: str
    name: str | None
    description: str | None
    contract_metadata: ContractMetadata | None

    class Config:
        orm_mode = True

    @root_validator(pre=True)
    def split_address(cls, values: dict) -> dict:
        if "workchain_id" not in values and "account_id" not in values:
            values["workchain_id"], values["account_id"] = values["address"].split(":")
        return values

    @classmethod
    def from_orm(cls, db_obj):
        setattr(db_obj, "address", f"{db_obj.workchain_id}:{db_obj.account_id}")
        return super().from_orm(db_obj)
