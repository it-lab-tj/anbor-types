from datetime import date
from decimal import Decimal
from typing import Annotated, Optional, Tuple

from anbor_types import ListQuery, Query
from anbor_types.catalog.enums import CatalogEntryKindEnum
from anbor_types.common.annotated import ATDatetimeRN
from anbor_types.utils.filter.meta import FilterMeta
from anbor_types.utils.filter.types import FilterSpec

# The reporting window the best-selling top is read through. Spelled
# `date__rn` because that is the name every other report's period filter
# carries, and the frontend sends one filter for the whole dashboard; `field`
# names the column it actually means, since `business_document` has no `date`.
InventoryAnalyticsPeriod = Annotated[
    Tuple[Optional[date], Optional[date]],
    FilterSpec.date_range(field="shipped_at", both_required=True),
]


class InventoryAnalyticsOverviewQuery(Query): ...


class InventoryAnalyticsCategoryFlowQuery(Query): ...


class InventoryAnalyticsLiquidQuery(ListQuery, metaclass=FilterMeta):
    date__rn: InventoryAnalyticsPeriod


class InventoryAnalyticsIlliquidQuery(ListQuery):
    """Pagination only.

    Staleness is measured back from now(), so there is no window to pass: a
    period filter could only move the threshold, and a report of "what is
    sitting on the shelf today" has no use for that. It carried a `date__rn`
    until 2026-11-03.
    """


# The window the top is read over, on `shipped_at`. Dates rather than
# datetimes, like the other reports here: the last day is then taken whole, and
# a `datetime` bound of `2026-11-04` would mean 00:00 and silently drop that
# day's sales.
#
# `required` without `both_required`: the caller must say when the period
# starts, and may leave the end open -- "from the first of the month until now"
# is the shape the dashboard asks for, and an open end saves it from sending
# today's date on every poll.
TopSellingPeriod = Annotated[
    Tuple[Optional[date], Optional[date]],
    FilterSpec.date_range(field="shipped_at", required=True),
]

# A bound on the SUMMED count per entry, so it compiles to HAVING rather than
# WHERE. The filter machinery only knows how to compile a column, so this spec
# is a parsing and documentation shape: the handler reads the tuple and hands it
# to the repository, and `parse_filters` is never called on this query.
TopSellingCountRange = Annotated[
    Tuple[Optional[Decimal], Optional[Decimal]],
    FilterSpec.numeric_range(base_type=Decimal, gte=Decimal(0)),
]


class TopSellingQuery(ListQuery, metaclass=FilterMeta):
    """Top of the best-selling catalog entries over a window.

    `entry_kind` is not optional: it decides which documents are read at all
    (products sell on SALE documents, services on SERVICE ones), and leaving it
    open meant no action filter -- which counted purchases, transfers and
    adjustments as "selling". It defaults to PRODUCT, the usual case.
    """

    date__rn: TopSellingPeriod
    sold_count__rn: TopSellingCountRange = (None, None)
    entry_kind: CatalogEntryKindEnum = CatalogEntryKindEnum.PRODUCT


class InventoryAnalyticsCashFlowQuery(Query, metaclass=FilterMeta):
    created_at__rn: ATDatetimeRN


class PerformerDocumentSummaryQuery(Query, metaclass=FilterMeta):
    shipped_at__rn: ATDatetimeRN
