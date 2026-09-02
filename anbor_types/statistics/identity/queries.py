from decimal import Decimal
from typing import Annotated, Tuple

from pydantic import Field

from anbor_types import ID_T, Query
from anbor_types.api.constants import DECIMAL_ZERO, ID_MAX
from anbor_types.common.annotated import ATDatetimeRN
from anbor_types.common.constraints import (
    DECIMAL_DISCOUNT_DIGITS,
    DECIMAL_DISCOUNT_PLACES,
    DISCOUNT_MAX,
)
from anbor_types.utils.filter.meta import FilterMeta
from anbor_types.utils.filter.types import FilterSpec
from anbor_types.warehouse.constants.enums import BusinessDocumentActionEnum

# Document kinds a staff member can be credited for. The other three carry no
# meaningful "this person sold it" reading: the returns undo somebody else's
# document, and an adjustment is a stock correction rather than a deal.
STAFF_SUMMARY_ALLOWED_ACTIONS: Tuple[BusinessDocumentActionEnum, ...] = (
    BusinessDocumentActionEnum.SALE,
    BusinessDocumentActionEnum.PURCHASE,
    BusinessDocumentActionEnum.TRANSFER,
    BusinessDocumentActionEnum.SERVICE,
)


class StaffBusinessDocumentSummaryQuery(Query, metaclass=FilterMeta):
    """What one staff member turned over, and the commission share of it.

    Everything that narrows the document set is a `FilterSpec`, so it compiles
    through the shared filter pipeline. Only `percentage` is not: it does not
    select rows, it scales the answer.

    `user_id` filters on `created_by_id` -- the document's author is what makes
    it "this person's". Confirmation status and company scope are not filters
    at all: they are the repository's own invariants and the client may not
    relax them.
    """

    user_id: Annotated[
        ID_T,
        FilterSpec.numeric(
            int,
            field="created_by_id",
            required=True,
            lte=ID_MAX,
            description="ID сотрудника (автора документов)",
        ),
    ]

    action: Annotated[
        BusinessDocumentActionEnum,
        FilterSpec.enum(
            BusinessDocumentActionEnum,
            required=True,
            choices=STAFF_SUMMARY_ALLOWED_ACTIONS,
            description=(
                "**0** — Продажа\n"
                "**1** — Закупка\n"
                "**2** — Перемещение\n"
                "**6** — Услуга\n"
            ),
        ),
    ]

    # Bounds the document's business date, inclusive on both ends. Not
    # `created_at`: a backdated document belongs to the period it shipped in.
    shipped_at__rn: ATDatetimeRN

    percentage: Annotated[
        Decimal,
        Field(
            max_digits=DECIMAL_DISCOUNT_DIGITS,
            decimal_places=DECIMAL_DISCOUNT_PLACES,
            ge=DECIMAL_ZERO,
            le=DISCOUNT_MAX,
            description="Процент начисления",
        ),
    ]
