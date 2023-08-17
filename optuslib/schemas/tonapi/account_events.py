from pydantic import BaseModel, Field


# https://tonapi.io/v1/event/getAccountEvents


class Price(BaseModel):
    token_name: str
    value: str


class Refund(BaseModel):
    origin: str
    type: str


class Collection(BaseModel):
    address: str
    name: str


class ImagePreview(BaseModel):
    resolution: str
    url: str


class AccountAddress(BaseModel):
    address: str
    icon: str | None
    is_scam: bool
    name: str | None


class Sale(BaseModel):
    address: str
    market: AccountAddress
    owner: AccountAddress | None
    price: Price


class NftItemRepr(BaseModel):
    address: str
    approved_by: list[str]
    collection: Collection | None
    collection_address: str | None  # deprecated
    dns: str | None
    index: int
    metadata: dict
    owner: AccountAddress | None
    previews: list[ImagePreview] | None
    sale: Sale | None
    verified: bool


class Jetton(BaseModel):
    address: str
    decimals: int
    image: str | None
    name: str
    symbol: str
    verification: str | None


class AuctionBidAction(BaseModel):
    amount: Price
    auction_type: str
    beneficiary: AccountAddress
    bidder: AccountAddress
    nft: NftItemRepr | None


class ContractDeployAction(BaseModel):
    address: str
    deployer: AccountAddress
    interfaces: list[str] | None


class JettonTransferAction(BaseModel):
    amount: str
    comment: str | None
    jetton: Jetton
    recipient: AccountAddress | None
    recipients_wallet: str
    refund: Refund | None
    sender: AccountAddress | None
    senders_wallet: str


class NftItemTransferAction(BaseModel):
    comment: str | None
    nft: str
    payload: str | None
    recipient: AccountAddress | None
    refund: Refund | None
    sender: AccountAddress | None


class NftPurchase(BaseModel):
    amount: Price
    buyer: AccountAddress
    nft: NftItemRepr
    purchase_type: str | None
    seller: AccountAddress


class SubscriptionAction(BaseModel):
    amount: int
    beneficiary: AccountAddress
    initial: bool
    subscriber: AccountAddress
    subscription: str


class TonTransferAction(BaseModel):
    amount: int
    comment: str | None
    payload: str | None
    recipient: AccountAddress
    refund: Refund | None
    sender: AccountAddress


class UnSubscriptionAction(BaseModel):
    beneficiary: AccountAddress
    subscriber: AccountAddress
    subscription: str


class ActionSimplePreview(BaseModel):
    full_description: str
    image: str | None
    name: str
    short_description: str


class Action(BaseModel):
    auction_bid: AuctionBidAction | None = Field(alias="AuctionBid")
    contract_deploy: ContractDeployAction | None = Field(alias="ContractDeploy")
    jetton_transfer: JettonTransferAction | None = Field(alias="JettonTransfer")
    nft_item_transfer: NftItemTransferAction | None = Field(alias="NftItemTransfer")
    nft_purchase: NftPurchase | None = Field(alias="NftPurchase")
    subscribe: SubscriptionAction | None = Field(alias="Subscribe")
    ton_transfer: TonTransferAction | None = Field(alias="TonTransfer")
    unsubscribe: UnSubscriptionAction | None = Field(alias="UnSubscribe")
    simple_preview: ActionSimplePreview
    status: str
    type: str

    class Config:
        allow_population_by_field_name = True


class Fee(BaseModel):
    account: AccountAddress
    deposit: int
    gas: int
    refund: int
    rent: int
    total: int


class AccountEvent(BaseModel):
    account: AccountAddress
    actions: list[Action]
    event_id: str
    fee: Fee
    in_progress: bool
    is_scam: bool
    lt: int
    timestamp: int


class Events(BaseModel):
    events: list[AccountEvent]
    next_from: int | None
