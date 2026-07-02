from datetime import datetime
from decimal import Decimal
from typing import Annotated, Optional, Tuple

from anbor_types.api.annotated import ATSearch
from anbor_types.api.filter_specs import AFStatus
from pydantic import Field, field_validator

from anbor_types import ID_T, ListQuery, Query
from anbor_types.common.constraints import DATETIME_MAX
from src.app.shared_kernel.constants.entity_common_constraints import PRICE_MAX, ID_MAX
from anbor_types.utils.filter.types import FilterSpec
from anbor_types.utils.filter.meta import FilterMeta


class ProductDetailedQuery(Query):
    id: ID_T


class ProductListQuery(ListQuery, metaclass=FilterMeta):
    limit: int = Field(
        default=10,
        gt=0,
        le=1000,
    )

    search: Optional[ATSearch] = None

    measurement_unit_id: Annotated[
        ID_T,
        FilterSpec.numeric(
            int,
            lte=ID_MAX,
        ),
    ]

    currency_id: Annotated[
        ID_T,
        FilterSpec.numeric(
            int,
            lte=ID_MAX,
        ),
    ]

    status: AFStatus

    buying_price__rn: Annotated[
        Tuple[Decimal, Decimal],
        FilterSpec.numeric_range(
            Decimal,
            lte=PRICE_MAX,
        ),
    ]

    selling_price__rn: Annotated[
        Tuple[Decimal, Decimal],
        FilterSpec.numeric_range(
            Decimal,
            lte=PRICE_MAX,
            gt=Decimal("0"),
        ),
    ]

    minimum_price__rn: Annotated[
        Tuple[Decimal, Decimal],
        FilterSpec.numeric_range(Decimal, lte=PRICE_MAX, gt=Decimal("0")),
    ]

    created_at: Annotated[
        datetime,
        FilterSpec.datetime_range(
            lte=DATETIME_MAX,
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
