from datetime import date
from decimal import Decimal
from typing import Annotated, Optional, Tuple

from pydantic import Field, field_validator

from anbor_types import ID_T, Query
from anbor_types.api.constants import DECIMAL_ZERO
from anbor_types.common.constraints import (
    DECIMAL_DISCOUNT_DIGITS,
    DECIMAL_DISCOUNT_PLACES,
    DISCOUNT_MAX,
)
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


class StaffBusinessDocumentSummaryQuery(Query):
    """What one staff member turned over, and the commission share of it.

    Sums the *confirmed* documents of a single kind that the given user
    authored, and returns ``percentage`` of that total alongside it.

    ``date_after`` / ``date_before`` bound the document's business date
    (``shipped_at``), not the row's creation timestamp, and are inclusive on
    both ends -- a request for a single day returns that whole day.
    """

    user_id: ID_T

    action: BusinessDocumentActionEnum

    percentage: Annotated[
        Decimal,
        Field(
            max_digits=DECIMAL_DISCOUNT_DIGITS,
            decimal_places=DECIMAL_DISCOUNT_PLACES,
            ge=DECIMAL_ZERO,
            le=DISCOUNT_MAX,
        ),
    ]

    date_after: Optional[date] = None
    date_before: Optional[date] = None

    @field_validator("action", mode="after")
    @classmethod
    def validate_action(
        cls, v: BusinessDocumentActionEnum
    ) -> BusinessDocumentActionEnum:
        if v not in STAFF_SUMMARY_ALLOWED_ACTIONS:
            allowed = ", ".join(str(int(a)) for a in STAFF_SUMMARY_ALLOWED_ACTIONS)
            raise ValueError(f"Allowed actions are: {allowed}")

        return v
