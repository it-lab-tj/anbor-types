from decimal import Decimal
from enum import IntEnum
from typing import Annotated, Optional, Tuple

from pydantic import StringConstraints
from anbor_types import ID_T, ListQuery, Query
from anbor_types.api.queries import ShortListQuery
from anbor_types.common.annotated import ATDatetimeRN
from anbor_types.common.enums import StatusEnum
from anbor_types.utils.filter.meta import FilterMeta
from anbor_types.utils.mixins import OrderingQueryMixin

from anbor_types.wallet.constraints import SUBJECT_BALANCE_MAX, SUBJECT_BALANCE_MIN
from anbor_types.warehouse.constants.enums import SubjectKindEnum
from anbor_types.utils.filter.types import FilterSpec
from anbor_types.api.constants import DECIMAL_ZERO, ID_MAX, PRICE_MAX


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


class SubjectStockProductsListQuery(
    ListQuery, OrderingQueryMixin, metaclass=FilterMeta
):
    """Products currently stocked in a given warehouse (subject of kind STORAGE),
    aggregated per (product, variant) across all inventory lots.

    `id` is the warehouse id and comes from the URL path, not from query params.
    """

    _ordering_allowed_fields = {"name", "remains", "cost_price", "last_sold_date"}

    id: ID_T

    search: Annotated[
        str,
        StringConstraints(max_length=100, strip_whitespace=True),
        FilterSpec.string(max_length=100),
    ]

    status: Annotated[StatusEnum, FilterSpec.enum(StatusEnum)]

    cost_price__rn: Annotated[
        Tuple[Decimal, Decimal],
        FilterSpec.numeric_range(
            Decimal,
            gte=DECIMAL_ZERO,
            description="Range filter over the aggregated cost price "
            "(`sum(price * remains)`) of a product in the warehouse.",
        ),
    ]


class SubjectRebalanceHistoryListQuery(ListQuery):
    # Comes from the URL path, not from query params.
    id: ID_T


class SubjectClientHistoryListQuery(ListQuery, metaclass=FilterMeta):
    class SubjectClientHistoryEnum(IntEnum):
        EXPENSE = 0
        INCOME = 1
        RECALCULATE = 3

    cash_desk_id: Optional[
        Annotated[
            ID_T,
            FilterSpec.numeric(
                int,
                lte=ID_MAX,
            ),
        ]
    ] = None

    id: Optional[
        Annotated[
            ID_T,
            FilterSpec.numeric(
                int,
                lte=ID_MAX,
            ),
        ]
    ] = None

    created_by_id: Optional[
        Annotated[
            ID_T,
            FilterSpec.numeric(
                int,
                lte=ID_MAX,
            ),
        ]
    ] = None

    currency_id: Optional[
        Annotated[
            ID_T,
            FilterSpec.numeric(
                int,
                lte=ID_MAX,
            ),
        ]
    ] = None

    operating_expense_id: Optional[
        Annotated[
            ID_T,
            FilterSpec.numeric(
                int,
                lte=ID_MAX,
            ),
        ]
    ] = None

    kind: Optional[
        Annotated[
            SubjectClientHistoryEnum,
            FilterSpec.enum(SubjectClientHistoryEnum),
        ]
    ] = None

    business_document_id: Optional[
        Annotated[
            ID_T,
            FilterSpec.numeric(
                int,
                lte=ID_MAX,
            ),
        ]
    ] = None

    amount__rn: Annotated[
        Tuple[Decimal, Decimal],
        FilterSpec.numeric_range(
            Decimal,
            lte=PRICE_MAX,
            gt=DECIMAL_ZERO,
        ),
    ]

    project_id: Optional[
        Annotated[
            ID_T,
            FilterSpec.numeric(
                int,
                lte=ID_MAX,
            ),
        ]
    ] = None

    created_at__rn: ATDatetimeRN
