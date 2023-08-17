from enum import Enum


class Period(str, Enum):
    DAY = "day"
    WEEK = "7D"
    MONTH = "1M"
    YEAR = "1Y"
    ALL = "ALL"
