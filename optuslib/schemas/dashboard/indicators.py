from decimal import Decimal
from math import floor, log10

from pydantic import BaseModel, validator

from ...constants import (
    CHANGE_ROUND_DECIMALS,
    USD_LIQUIDITY_ROUND_DECIMALS,
    USD_VOLUME_ROUND_DECIMALS,
    FEE_ROUND_DECIMALS,
    APR_ROUND_DECIMALS,
    LIQUIDITY_ROUND_SIGNIFICANT,
    PRICE_ROUND_SIGNIFICANT,
    AMOUNT_ROUND_SIGNIFICANT,
)


class Indicator(BaseModel):
    value: str = "0"
    change: str = "--"

    @validator("change", pre=True)
    def check_change(cls, value: float | str) -> str:
        if value is None:
            return "--"
        elif isinstance(value, str):
            return value
        else:
            return str(round(value, CHANGE_ROUND_DECIMALS))

    @validator("value", pre=True)
    def round_value(cls, value: float | int | str | None) -> str:
        if value is None:
            return "0"
        elif isinstance(value, str):
            return value
        else:
            return format(cls._calc_value(value), ".20f").rstrip("0").rstrip(".")

    @classmethod
    def add_value(cls, value: float | int, decimals: int | None = None):
        if decimals:
            value = value / 10**decimals

        return cls(value=value, change=None)

    @classmethod
    def from_map(cls, value_map: dict[int, float], decimals: int = 0):
        days = sorted(value_map.keys())
        if days:
            value = (value_map.get(days[-1]) / 10**decimals) if decimals else value_map.get(days[-1])
        else:
            value = None
        if len(days) > 1 and value_map.get(days[-2]):
            change = (value_map.get(days[-1]) / value_map.get(days[-2]) - 1) * 100
        else:
            change = None
        return cls(value=value, change=change)

    @classmethod
    def _round_significant(cls, value: Decimal, sig: int) -> Decimal:
        if value == 0:
            return value
        else:
            return round(value, sig - int(floor(log10(abs(value)))) - 1)

    @classmethod
    def _calc_value(cls, value: float | int) -> Decimal:
        return Decimal(value)


class LiquidityIndicator(Indicator):
    @classmethod
    def _calc_value(cls, value: float | int) -> Decimal:
        return cls._round_significant(Decimal(value), LIQUIDITY_ROUND_SIGNIFICANT)


class UsdLiquidityIndicator(Indicator):
    @classmethod
    def _calc_value(cls, value: float | int) -> Decimal:
        return round(Decimal(value), USD_LIQUIDITY_ROUND_DECIMALS)


class UsdVolumeIndicator(Indicator):
    @classmethod
    def _calc_value(cls, value: float | int) -> Decimal:
        return round(Decimal(value), USD_VOLUME_ROUND_DECIMALS)


class PriceIndicator(Indicator):
    @classmethod
    def _calc_value(cls, value: float | int) -> Decimal:
        return cls._round_significant(Decimal(value), PRICE_ROUND_SIGNIFICANT)


class FeeIndicator(Indicator):
    @classmethod
    def _calc_value(cls, value: float | int) -> Decimal:
        return round(Decimal(value), FEE_ROUND_DECIMALS)


class AprIndicator(Indicator):
    @classmethod
    def _calc_value(cls, value: float | int) -> Decimal:
        return round(Decimal(value), APR_ROUND_DECIMALS)


class AmountIndicator(Indicator):
    @classmethod
    def _calc_value(cls, value: float | int) -> Decimal:
        return cls._round_significant(Decimal(value), AMOUNT_ROUND_SIGNIFICANT)


class UsdLiquidity(BaseModel):
    ton: UsdLiquidityIndicator = UsdLiquidityIndicator()
    usd: UsdLiquidityIndicator = UsdLiquidityIndicator()


class UsdVolume(BaseModel):
    ton: UsdVolumeIndicator = UsdVolumeIndicator()
    usd: UsdVolumeIndicator = UsdVolumeIndicator()


class UsdAmount(BaseModel):
    ton: AmountIndicator = AmountIndicator()
    usd: AmountIndicator = AmountIndicator()
