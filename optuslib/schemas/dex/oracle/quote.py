from pydantic import BaseModel

from ...base.base_models import BaseUserFriendlyAddressModel


class QuoteRequest(BaseUserFriendlyAddressModel):
    user_address: str
    from_token_address: str
    to_token_address: str
    from_token_amount: int | None
    to_token_amount: int | None
    slippage_tolerance: float


class QuoteProtocol(BaseModel):
    name: str
    from_token_amount: int
    to_token_amount: int


class QuoteMessage(BaseModel):
    address: str
    amount: int
    payload: str


class Quote(QuoteRequest):
    price_impact: float
    protocols: list[QuoteProtocol]
    messages: list[QuoteMessage]
    blockchain_fee: int
    aggregator_fee: int
