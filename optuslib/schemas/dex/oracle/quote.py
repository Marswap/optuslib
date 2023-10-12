from pydantic import BaseModel

from ...base.base_models import BaseRawAddressModel


class QuoteRequest(BaseRawAddressModel):
    user_address: str
    from_jetton_wallet_address: str
    from_address: str
    to_address: str
    from_amount: int | None
    to_amount: int | None
    slippage_tolerance: float


class QuoteProtocol(BaseModel):
    name: str
    part: int


class QuoteMessage(BaseModel):
    address: str
    amount: int
    payload: str


class Quote(QuoteRequest):
    price_impact: float
    protocols: list[QuoteProtocol]
    messages: list[QuoteMessage]
    blockchain_fee: int
