from ..schemas.dashboard.db.contract import Contract
from ..schemas.dashboard.db.contract_metadata import ContractMetadata

TON = Contract(
    address="0:0000000000000000000000000000000000000000000000000000000000000000",
    workchain_id=0,
    account_id="0000000000000000000000000000000000000000000000000000000000000000",
    contract_metadata=ContractMetadata(
        name="TON",
        image="https://cache.tonapi.io/imgproxy/TxOnfDl49UJhLnmbyTiOfHkfcckxe8jr_RuQbevucQk/rs:fill:200:200:1/g:no/aHR0cHM6Ly9zdGF0aWMuc3Rvbi5maS9sb2dvL3Rvbl9zeW1ib2wucG5n.webp",
        symbol="TON",
        decimals=9,
    ),
)
