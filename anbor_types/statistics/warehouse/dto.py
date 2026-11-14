from datetime import datetime

import msgspec
from decimal import Decimal
from typing import List, Optional, Tuple

from anbor_types import ListQueryResponse, ID_T
from anbor_types.common.dto import NameIdDTO
from anbor_types.gallery.dto import ImageMediumDTO


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

    ``days_without_sale`` is counted to now(), the same instant the staleness
    threshold uses, so it agrees with the threshold that selected the row. It
    is null exactly when ``last_sold_at`` is -- stock that has never been sold
    has no last sale to count from, and inventing a number from the receipt
    date would mean something different from every other row.

    ``last_sold_at`` is kept alongside it: null for a product never sold at all.
    Stock that has never moved is the most illiquid there is, so it belongs in
    this list rather than outside it.

    ``frozen_amount`` is what the remaining stock cost to acquire
    (``Σ remains × lot price``, base currency), not what it would sell for.

    ``images`` holds the product's first image, or nothing -- a collection so
    the field keeps the shape every other catalog surface sends, and so a
    second one can be added without a contract change. An image whose medium
    render is missing is left out rather than sent with a null URL: there is
    nothing to draw either way, and ``medium_url`` stays a plain ``str``.
    """

    product_id: ID_T
    product_name: str
    remains: Decimal
    frozen_amount: Decimal
    last_sold_at: Optional[datetime] = None
    days_without_sale: Optional[int] = None
    images: Tuple[ImageMediumDTO, ...] = ()


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


class TopSellingEntryDTO(msgspec.Struct):
    """One row of the best-selling top, over the requested window.

    ``sold_count`` is units, not documents -- the sum of the line counts, so a
    receipt for ten pieces contributes ten. ``revenue`` is what those lines
    charged in company currency: price x count, less the line discount, at the
    document's rate. The same expression every other report in this boundary
    uses, so two panels cannot disagree about one product's takings.
    """

    entry_id: ID_T
    entry_name: str
    sold_count: Decimal
    revenue: Decimal
    images: Tuple[ImageMediumDTO, ...] = ()


class TopSellingListDTO(ListQueryResponse[TopSellingEntryDTO]):
    """The top plus its footer total.

    ``count``, ``total_sold_count`` and ``total_revenue`` describe the WHOLE
    selection rather than the returned page, and all three are read off the
    same grouped subquery the rows come from -- including the
    ``sold_count__rn`` bound. A footer counted over one set and summed over
    another would simply be wrong.

    ``rows`` is redeclared, identically to what the generic already says: the
    OpenAPI generator does not follow a type parameter through a subclass, so
    without this the schema documents the rows as bare objects and the frontend
    loses every field name.
    """

    rows: List[TopSellingEntryDTO]
    total_sold_count: Decimal
    total_revenue: Decimal


class InventoryAnalyticsCashFlowDTO(msgspec.Struct):
    income: Decimal
    expense: Decimal
    # Cost of goods sold over the same window, at lot cost -- the same basis as
    # the income statement's `cost_price`.
    sold_cost: Decimal


class PerformerSummaryDTO(msgspec.Struct):
    performer: NameIdDTO
    service_completed: Decimal
    revenue: Decimal
    commission: Decimal
    revenue_commission: Decimal
