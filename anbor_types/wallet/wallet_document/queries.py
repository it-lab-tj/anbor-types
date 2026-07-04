from datetime import datetime
from decimal import Decimal
from typing import Annotated, Optional, Tuple

from anbor_types import ID_T, ListQuery, Query
from anbor_types.api.annotated import ATSearch
from anbor_types.api.types import OrderingAllowedFieldsT
from anbor_types.common.constraints import DATETIME_MAX
from anbor_types.utils.mixins import OrderingQueryMixin
from anbor_types.wallet.constants import WalletDocumentKindEnum
from anbor_types.api.constants import PRICE_MAX, ID_MAX
from anbor_types.utils.filter.types import FilterSpec
from anbor_types.utils.filter.meta import FilterMeta


class WalletDocumentDetailedQuery(Query):
    id: ID_T


class WalletTransferListQuery(ListQuery, OrderingQueryMixin, metaclass=FilterMeta):
    _ordering_allowed_fields: OrderingAllowedFieldsT = {"created_at", "amount"}

    # Filters transfers where the desk is either the source or the destination.
    cash_desk_id: Annotated[
        ID_T,
        FilterSpec.numeric(
            int,
            lte=ID_MAX,
        ),
    ]

    operating_expense_id: Annotated[
        ID_T,
        FilterSpec.numeric(
            int,
            lte=ID_MAX,
        ),
    ]

    amount__rn: Annotated[
        Tuple[Decimal, Decimal],
        FilterSpec.numeric_range(
            Decimal,
            lte=PRICE_MAX,
            gt=Decimal("0"),
        ),
    ]

    created_by_id: Annotated[
        ID_T, FilterSpec.numeric(int, lte=ID_MAX, description="По создателю документа")
    ]

    created_at__rn: Annotated[
        datetime,
        FilterSpec.datetime_range(
            lte=DATETIME_MAX,
        ),
    ]


class WalletDocumentListQuery(ListQuery, OrderingQueryMixin, metaclass=FilterMeta):
    search: Optional[ATSearch] = None
    _ordering_allowed_fields: OrderingAllowedFieldsT = {"created_at", "amount"}

    cash_desk_id: Annotated[
        ID_T,
        FilterSpec.numeric(
            int,
            lte=ID_MAX,
        ),
    ]

    counterparty_id: Annotated[
        ID_T,
        FilterSpec.numeric(
            int,
            lte=ID_MAX,
        ),
    ]

    created_by_id: Annotated[
        ID_T,
        FilterSpec.numeric(
            int,
            lte=ID_MAX,
        ),
    ]

    updated_by_id: Annotated[
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

    operating_expense_id: Annotated[
        ID_T,
        FilterSpec.numeric(
            int,
            lte=ID_MAX,
        ),
    ]

    kind: Annotated[
        WalletDocumentKindEnum,
        FilterSpec.enum(WalletDocumentKindEnum),
    ]

    amount__rn: Annotated[
        Tuple[Decimal, Decimal],
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
