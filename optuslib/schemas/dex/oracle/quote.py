from pydantic import BaseModel

from ...base.base_models import BaseUserFriendlyAddressModel


class QuoteRequest(BaseUserFriendlyAddressModel):
    user_address: str = "EQC5aj2p6ClvTKx2-jWjSBrYbWTS_S2moHW4mRh2QOq1Um6x"
    from_token_address: str = "EQDCJL0iQHofcBBvFBHdVG233Ri2V4kCNFgfRT-gqAd3Oc86"
    to_token_address: str = "EQDQoc5M3Bh8eWFephi9bClhevelbZZvWhkqdo80XuY_0qXv"
    from_jetton_wallet_address: str = "EQDgqKCh2UeenPS6g-jHnv_tbli1ilXDdkYHaBoVxKXBSaZD"
    from_token_amount: int = 100000000000
    slippage_tolerance: float = 0.1


class QuoteProtocol(BaseModel):
    name: str
    from_token_amount: int
    to_token_amount: int


class QuoteMessage(BaseModel):
    address: str
    amount: int
    payload: str


class Quote(QuoteRequest):
    to_token_amount: int
    price_impact: float
    protocols: list[QuoteProtocol]
    messages: list[QuoteMessage]
    blockchain_fee: int
    aggregator_fee: int
