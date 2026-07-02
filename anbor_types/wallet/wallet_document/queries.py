from datetime import datetime
from decimal import Decimal
from typing import Annotated, List, Optional, Tuple

from anbor_types import ID_T, ListQuery
from anbor_types.api.annotated import ATSearch
from anbor_types.common.constraints import DATETIME_MAX
from anbor_types.wallet.constants import WalletDocumentKindEnum
from src.app.shared_kernel.constants.entity_common_constraints import PRICE_MAX, ID_MAX
from anbor_types.utils.filter.types import FilterSpec
from anbor_types.utils.filter.meta import FilterMeta


class WalletTransferListQuery(ListQuery, metaclass=FilterMeta):
    # Filters transfers where the desk is either the source or the destination.
    cash_desk_id: Annotated[
        ID_T,
        FilterSpec.numeric(
            int,
            lte=ID_MAX,
        ),
    ]

    created_at: Annotated[
        datetime,
        FilterSpec.datetime_range(
            lte=DATETIME_MAX,
        ),
    ]

    # Sort spec, not a filter — left plain so it stays an opaque query param.
    ordering: Optional[str] = None


class WalletDocumentListQuery(ListQuery, metaclass=FilterMeta):
    search: Optional[ATSearch] = None

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

    project_id: Annotated[
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

    created_at: Annotated[
        datetime,
        FilterSpec.datetime_range(
            lte=DATETIME_MAX,
        ),
    ]

    ordering: Optional[str] = None

    # IN-over-list has no FilterSpec factory yet; kept plain until one exists.
    vendor_codes: Optional[List[str]] = None
