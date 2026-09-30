from datetime import datetime

import msgspec
from decimal import Decimal
from typing import List, Optional

from anbor_types import ListQueryResponse
from anbor_types.common.dto import NameIdDTO


class InventoryAnalyticsOverviewDTO(msgspec.Struct):
    products_count: Decimal
    created_product_count: Decimal
    warehouse_stock_cost: Decimal
    deficit_count: Decimal
    frozen_capital: Decimal


class StockByCategoryDTO(msgspec.Struct):
    category_name: str
    total_cost: Decimal


class InventoryAnalyticsCategoryFlowDTO(msgspec.Struct):
    stock_by_category: List[StockByCategoryDTO]


class InventoryAnalyticsLiquidDTO(msgspec.Struct):
    """One row of the best-selling top, scoped to the requested period.

    ``last_sold_at`` is never null here: a product only reaches this list by
    having sold inside the period. It is a `datetime`, and always has been on
    the wire -- it is `max(shipped_at)`, a timestamptz. Declaring it as a
    `date` only made the OpenAPI schema claim `format: date` for a value the
    API has always sent as a full timestamp; nothing about the response
    changed with this.

    ``revenue_change_percent`` compares ``revenue`` against the equally long
    window immediately before the requested one. It is null -- not zero --
    when that window earned nothing, because a rise from nothing has no
    percentage.
    """

    product_name: str
    last_sold_at: datetime
    sales_count: int
    revenue: Decimal
    revenue_change_percent: Optional[Decimal]


class InventoryAnalyticsIlliquidDTO(msgspec.Struct):
    """One row of the stale-stock top.

    ``last_sold_at`` is null for a product that has never been sold at all --
    stock that has never moved is the most illiquid there is, so it belongs in
    this list rather than outside it. The frontend derives "N days without a
    sale" from this field and has to render that null case.

    ``frozen_amount`` is what the remaining stock cost to acquire
    (``Σ remains × lot price``, base currency), not what it would sell for.
    ``revenue`` covers the requested period, so it is 0 whenever that period is
    no longer than the staleness threshold -- nothing in this list sold inside
    such a window, by construction.
    """

    product_name: str
    last_sold_at: Optional[datetime]
    remains: Decimal
    frozen_amount: Decimal
    revenue: Decimal


class InventoryAnalyticsIlliquidListDTO(
    ListQueryResponse[InventoryAnalyticsIlliquidDTO]
):
    """The stale-stock list plus its footer total.

    ``count`` and ``total_frozen_amount`` describe the WHOLE selection, not the
    returned page -- together they are the
    "ВСЕГО: 5 товаров · на сумму 17 400 смн заморожено" line, so the frontend
    does not have to pull every row down to add them up.

    ``rows`` is redeclared, identically to what the generic already says: the
    OpenAPI generator does not follow a type parameter through a subclass, so
    without this the schema documents the rows as bare objects and the frontend
    loses every field name. Field order is unaffected -- a redeclared field
    keeps its inherited position.
    """

    rows: List[InventoryAnalyticsIlliquidDTO]
    total_frozen_amount: Decimal


class InventoryAnalyticsCashFlowDTO(msgspec.Struct):
    income: Decimal
    expense: Decimal


class PerformerSummaryDTO(msgspec.Struct):
    performer: NameIdDTO
    service_completed: Decimal
    revenue: Decimal
    commission: Decimal
    revenue_commission: Decimal
