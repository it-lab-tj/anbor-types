from datetime import date
from decimal import Decimal
from typing import Optional

import msgspec


class DailyAnalyticsDTO(msgspec.Struct):
    id: int
    date: Optional[date]
    revenues: Decimal
    expenses: Decimal
    realisations: Decimal
    cash_desk_balance: Decimal
