from pydantic import Field, field_validator
from anbor_types import ListQuery


class ProductListQuery(ListQuery): ...


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

    @field_validator
    def validate_limit(self, v) -> int:
        return min(v, 10000) if v > 0 else 0
