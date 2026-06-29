from pydantic import Field, field_validator
from anbor_types import ListQuery

# from src.app.shared_kernel.utils.filters.types import FilterFieldSpec


class ProductListQuery(ListQuery):
    # filters: Tuple[FilterFieldSpec, ...] = Field(default_factory=tuple, init=False)
    pass


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
