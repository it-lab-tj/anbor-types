from datetime import date
from decimal import Decimal
from typing import Optional

from anbor_types import Query


class DailyAnalyticListQuery(Query):
    date_after: Optional[date] = None,
    date_before: Optional[date] = None,
    realisations_max: Optional[Decimal] = None,
    realisations_min: Optional[Decimal] = None,
    revenues_max: Optional[Decimal] = None,
    revenues_min: Optional[Decimal] = None,
