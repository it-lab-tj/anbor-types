from datetime import datetime
from typing import Annotated

from anbor_types import Query
from anbor_types.common.annotated import ATFilterRangeRequired
from anbor_types.utils.filter import FilterSpec, FilterMeta


class CompanyAnalyticsSummaryQuery(Query):
    """Analytic of company's summary about subject's types, and some money-totals"""


class CompanyAnalyticsMoneySummaryQuery(Query, metaclass=FilterMeta):
    """Analytic only about company's money-totals (profit, revenue, sales, ...)"""

    period__rn: Annotated[
        ATFilterRangeRequired[datetime], FilterSpec.datetime_range(both_required=True)
    ]
