from decimal import Decimal
from typing import Annotated

from anbor_types.warehouse.constants.constraints import PRICE_MAX

from anbor_types.utils.filter.types import FilterSpec
from pydantic import Field, field_validator

from anbor_types import ID_T, ListQuery, Query
from anbor_types.catalog.catalog_entry.queries import CatalogEntryBaseListQuery


class ProductDetailedQuery(Query):
    id: ID_T


class ProductListQuery(CatalogEntryBaseListQuery):
    buying_price__rn: Annotated[
        Decimal,
        FilterSpec.numeric_range(
            Decimal,
            lte=PRICE_MAX,
            gt=Decimal("0"),
        ),
    ]


class ProductDetailedListQuery(ListQuery):
    limit: int = Field(
        default=0,
        gt=0,
        lt=10000,
    )

    offset: int = Field(
        default=0,
        gt=-1,
    )

    @field_validator("limit")
    @classmethod
    def validate_limit(cls, v) -> int:
        return min(v, 10000) if v >= 1 else 1
