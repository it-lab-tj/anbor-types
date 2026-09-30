from datetime import date
from typing import Annotated, Optional, Tuple

from anbor_types import ListQuery, Query
from anbor_types.common.annotated import ATDatetimeRN
from anbor_types.utils.filter.meta import FilterMeta
from anbor_types.utils.filter.types import FilterSpec

# The reporting window both top-lists are read through. Spelled `date__rn`
# because that is the name every other report's period filter carries, and the
# frontend sends one filter for the whole dashboard; `field` names the column it
# actually means, since `business_document` has no `date`.
InventoryAnalyticsPeriod = Annotated[
    Tuple[Optional[date], Optional[date]],
    FilterSpec.date_range(field="shipped_at", both_required=True),
]


class InventoryAnalyticsOverviewQuery(Query): ...


class InventoryAnalyticsCategoryFlowQuery(Query): ...


class InventoryAnalyticsLiquidQuery(ListQuery, metaclass=FilterMeta):
    date__rn: InventoryAnalyticsPeriod


class InventoryAnalyticsIlliquidQuery(ListQuery, metaclass=FilterMeta):
    date__rn: InventoryAnalyticsPeriod


class InventoryAnalyticsCashFlowQuery(Query, metaclass=FilterMeta):
    created_at__rn: ATDatetimeRN


class PerformerDocumentSummaryQuery(Query, metaclass=FilterMeta):
    shipped_at__rn: ATDatetimeRN
