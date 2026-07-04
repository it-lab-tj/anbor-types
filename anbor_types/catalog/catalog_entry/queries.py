from datetime import datetime
from decimal import Decimal
from typing import Annotated, Optional


from anbor_types import ID_T, ListQuery
from anbor_types.api.types import OrderingAllowedFieldsT
from anbor_types.common.constraints import DATETIME_MAX
from anbor_types.common.enums import StatusEnum
from anbor_types.utils.filter.meta import FilterMeta, FilterSpec
from anbor_types.utils.mixins import OrderingQueryMixin
from src.app.shared_kernel.constants.entity_common_constraints import ID_MAX, PRICE_MAX
from anbor_types.api.annotated import AFSearch


class CatalogEntryBaseListQuery(ListQuery, OrderingQueryMixin, metaclass=FilterMeta):
    _ordering_allowed_fields: OrderingAllowedFieldsT = {"name", "created_at"}

    search: Optional[AFSearch] = None

    measurement_unit_id: Annotated[
        ID_T,
        FilterSpec.numeric(
            int,
            lte=ID_MAX,
        ),
    ]

    currency_id: Annotated[
        ID_T,
        FilterSpec.numeric(int, lte=ID_MAX),
    ]

    status: Annotated[
        StatusEnum,
        FilterSpec.numeric(
            StatusEnum,
            choices=StatusEnum,
        ),
    ]

    selling_price__rn: Annotated[
        Decimal,
        FilterSpec.numeric_range(
            Decimal,
            lte=PRICE_MAX,
            gt=Decimal("0"),
        ),
    ]

    minimum_price__rn: Annotated[
        Decimal,
        FilterSpec.numeric_range(
            Decimal,
            lte=PRICE_MAX,
            gt=Decimal("0"),
        ),
    ]

    created_at__rn: Annotated[
        datetime,
        FilterSpec.datetime_range(
            lte=DATETIME_MAX,
        ),
    ]
