from decimal import Decimal
from typing import Annotated, Tuple

from pydantic import StringConstraints

from anbor_types import ID_T, ListQuery, Query
from anbor_types.api.queries import ShortListQuery
from anbor_types.common.enums import StatusEnum
from anbor_types.utils.filter.meta import FilterMeta
from anbor_types.utils.mixins import OrderingQueryMixin

from anbor_types.wallet.constraints import SUBJECT_BALANCE_MAX, SUBJECT_BALANCE_MIN
from anbor_types.warehouse.constants.enums import SubjectKindEnum
from anbor_types.utils.filter.types import FilterSpec


class SubjectListQuery(ListQuery, OrderingQueryMixin, metaclass=FilterMeta):
    _ordering_allowed_fields = {"created_at", "name"}

    kind: Annotated[
        SubjectKindEnum,
        FilterSpec.enum(
            SubjectKindEnum,
            description="**1** - Склад\n" "**2** - Клиент\n" "**3** - Исполнитель\n",
            required=True,
        ),
    ]
    status: Annotated[StatusEnum, FilterSpec.enum(StatusEnum, required=True)]

    balance__rn: Annotated[
        Tuple[Decimal, Decimal],
        FilterSpec.numeric_range(
            Decimal,
            lte=SUBJECT_BALANCE_MAX,
            gte=SUBJECT_BALANCE_MIN,
        ),
    ]

    search: Annotated[
        str,
        StringConstraints(max_length=100, strip_whitespace=True),
        FilterSpec.string(max_length=100),
    ]


class SubjectShortListQuery(ShortListQuery):
    kind: Annotated[
        SubjectKindEnum,
        FilterSpec.enum(
            SubjectKindEnum,
            description="**1** - Склад\n" "**2** - Клиент\n" "**3** - Исполнитель\n",
        ),
    ]


class SubjectDetailedQuery(Query):
    id: ID_T


class SubjectBalanceQuery(Query):
    id: ID_T


class SubjectStockProductsQuery(Query):
    id: ID_T


class SubjectRebalanceHistoryListQuery(ListQuery):
    # Comes from the URL path, not from query params.
    id: ID_T
