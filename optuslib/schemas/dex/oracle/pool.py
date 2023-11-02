from pydantic import BaseModel


class OraclePoolJetton(BaseModel):
    minter_address: str | None
    wallet_address: str | None
    vault_address: str | None
    reserve: int | None


class OraclePoolData(BaseModel):
    jetton_0: OraclePoolJetton
    jetton_1: OraclePoolJetton
    fee: float


class OraclePool(BaseModel):
    id: int
    pool_data: OraclePoolData | None
