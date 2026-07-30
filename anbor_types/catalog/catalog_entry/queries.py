from decimal import Decimal
from typing import Annotated, Optional


from anbor_types import ID_T, ListQuery
from anbor_types.api.types import OrderingAllowedFieldsT
from anbor_types.common.annotated import ATDatetimeRN
from anbor_types.common.enums import StatusEnum
from anbor_types.utils.filter.meta import FilterMeta, FilterSpec
from anbor_types.utils.mixins import OrderingQueryMixin
from anbor_types.api.constants import ID_MAX, PRICE_MAX
from anbor_types.api.annotated import ATSearch


class CatalogEntryBaseListQuery(ListQuery, OrderingQueryMixin, metaclass=FilterMeta):
    _ordering_allowed_fields: OrderingAllowedFieldsT = {"name", "created_at"}

    # Not `Optional[AFSearch]`: wrapping `Annotated` into `Optional` hides
    # `FilterSpec` from FilterMeta and the parser, so the filter never fires.
    search: Annotated[Optional[ATSearch], FilterSpec.string()] = None

    category_id: Annotated[
        ID_T,
        FilterSpec.numeric(int, lte=ID_MAX),
    ]

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

    created_at__rn: ATDatetimeRN
