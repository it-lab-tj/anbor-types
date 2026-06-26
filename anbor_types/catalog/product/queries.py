from pydantic import Field, field_validator
from anbor_types import ID_T, ListQuery, Query
from src.app.shared_kernel.utils.filters.mixins import QueryFilterMixin


class ProductDetailedQuery(Query):
    id: ID_T


class ProductListQuery(ListQuery, QueryFilterMixin): ...


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
