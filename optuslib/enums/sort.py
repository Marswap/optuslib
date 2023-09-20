from enum import Enum


class Order(str, Enum):
    ASC = "asc"
    DESC = "desc"


class IndicatorField(str, Enum):
    VALUE = "value"
    CHANGE = "change"
