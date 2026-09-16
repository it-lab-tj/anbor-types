from decimal import Decimal
from typing import Annotated, List, Optional

from anbor_types.warehouse.constants.constraints import PRICE_MAX

from anbor_types.utils.filter.types import FilterSpec
from pydantic import Field, field_validator, PrivateAttr

from anbor_types import ID_T, ListQuery, Query
from anbor_types.catalog.catalog_entry.queries import CatalogEntryBaseListQuery
from anbor_types.catalog.category.dto import CharValueDTO
from anbor_types.catalog.constraints import CATALOG_ENTRY_VARIANT_CHAR_VALUES_MAX_COUNT
from anbor_types.api.constants import DECIMAL_ZERO


class ProductDetailedQuery(Query):
    id: ID_T


class ProductProfilesQuery(Query):
    product_id: ID_T


class ProductRemainsQuery(Query):
    _id: ID_T = PrivateAttr(init=False)
    storage_id: Optional[ID_T] = None
    char_values: List[CharValueDTO] = Field(
        default_factory=list,
        max_length=CATALOG_ENTRY_VARIANT_CHAR_VALUES_MAX_COUNT,
    )

    @property
    def id(self) -> ID_T:
        return self._id

    @field_validator("storage_id", mode="after")
    @classmethod
    def validate_storage_id(cls, v: Optional[ID_T]) -> Optional[ID_T]:
        # Ignore value `0` for front-end purpose: Naimjon
        if not v:
            return None
        return v


class ProductListQuery(CatalogEntryBaseListQuery):
    buying_price__rn: Annotated[
        Decimal,
        FilterSpec.numeric_range(
            Decimal,
            lte=PRICE_MAX,
            gt=DECIMAL_ZERO,
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
