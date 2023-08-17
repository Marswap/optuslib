from enum import Enum


class OperationType(str, Enum):
    SWAP = "swap"
    ADD = "add"
    REMOVE = "remove"
    OTHER = "other"
