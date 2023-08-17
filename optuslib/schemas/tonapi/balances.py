from pydantic import BaseModel

from .account_events import AccountAddress
from .info import JettonMetadata


# https://tonapi.io/v1/jetton/getBalances


class JettonBalance(BaseModel):
    balance: str
    jetton_address: str
    metadata: JettonMetadata
    verification: str
    wallet_address: AccountAddress


class JettonBalances(BaseModel):
    balances: list[JettonBalance]
