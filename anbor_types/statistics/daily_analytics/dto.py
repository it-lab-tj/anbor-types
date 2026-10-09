from datetime import date as Date, time as Time
from decimal import Decimal
from typing import Optional

import msgspec

from anbor_types import BasePydanticModel


class DailyAnalyticDTO(msgspec.Struct):
    date: Optional[Date]
    revenues: Decimal
    expenses: Decimal
    realisations: Decimal
    cash_desk_balance: Decimal


class DailyAnalyticByDateDTO(msgspec.Struct):
    hour: Optional[Time]
    revenues: Decimal
    expenses: Decimal
    realisations: Decimal
    cash_desk_balance: Decimal


class DailyAnalyticShortDTO(msgspec.Struct):
    revenue: Decimal
    expense: Decimal
    date: Date
    cash_desk_balance: Decimal


class DailyAnalyticUpdateDTO(BasePydanticModel):
    expense: Optional[Decimal] = None
    revenue: Optional[Decimal] = None
