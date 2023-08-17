from __future__ import annotations

from pydantic import BaseModel

from .account_events import AccountAddress


# https://tonapi.io/v1/trace/getAnnotatedTrace


class AnnotationData(BaseModel):
    balance_diff: int | None
    amount: str | None
    # comment: str | None  # давал ошибку при сохранении в БД
    from_address: str | None
    jetton_address: str | None
    destination_address: str | None
    forward_ton_amount: str | None
    query_id: int | None
    response_destination_address: str | None
    sender_address: str | None
    recipient_address: str | None
    recipients_wallet_address: str | None
    response_address: str | None
    senders_wallet_address: str | None
    deployer: str | None


class Annotation(BaseModel):
    data: AnnotationData
    name: str
    name: str

    class Config:
        use_enum_values = True


class Trace(BaseModel):
    account: AccountAddress
    annotations: list[Annotation] | None
    children: list[Trace] | None
    fee: int
    hash: str
    input_value: int
    interfaces: list[str] | None
    interfaces: list[str] | None
    lt: int
    other_fee: int
    storage_fee: int
    success: bool
