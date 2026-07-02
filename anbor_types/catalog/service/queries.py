from datetime import datetime
from decimal import Decimal
from typing import Annotated, Optional

from anbor_types import ListQuery, Query, ID_T
from anbor_types.api.annotated import ATSearch
from anbor_types.common.constraints import DATETIME_MAX
from anbor_types.common.enums import StatusEnum
from src.app.shared_kernel.constants.entity_common_constraints import PRICE_MAX, ID_MAX
from anbor_types.utils.filter.types import FilterSpec
from anbor_types.utils.filter.meta import FilterMeta


class ServiceDetailedQuery(Query):
    id: ID_T


class ServiceListQuery(ListQuery, metaclass=FilterMeta):
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
            int, lte=ID_MAX, description="Test description with `Markdown`"
        ),
    ]

    status: Annotated[
        StatusEnum,
        FilterSpec.numeric(
            StatusEnum,
            choices=StatusEnum,
        ),
    ]

    selling_price: Annotated[
        Decimal,
        FilterSpec.numeric_range(
            Decimal,
            lte=PRICE_MAX,
            gt=Decimal("0"),
        ),
    ]

    minimum_price: Annotated[
        Decimal,
        FilterSpec.numeric_range(
            Decimal,
            lte=PRICE_MAX,
            gt=Decimal("0"),
        ),
    ]

    created_at: Annotated[
        datetime,
        FilterSpec.datetime_range(
            lte=DATETIME_MAX,
        ),
    ]
