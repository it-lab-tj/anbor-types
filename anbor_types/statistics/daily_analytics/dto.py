from datetime import date
from decimal import Decimal
from typing import Optional

import msgspec

from anbor_types import BasePydanticModel


class DailyAnalyticDTO(msgspec.Struct):
    id: int
    date: Optional[date]
    revenues: Decimal
    expenses: Decimal
    realisations: Decimal
    cash_desk_balance: Decimal


class DailyAnalyticShortDTO(msgspec.Struct):
    revenue: Decimal
    expense: Decimal
    date: date
    cash_desk_balance: Decimal


class DailyAnalyticUpdateDTO(BasePydanticModel):
    expense: Optional[Decimal] = None
    revenue: Optional[Decimal] = None
