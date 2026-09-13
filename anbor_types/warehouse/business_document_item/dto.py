from datetime import date
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, Field

from anbor_types import ID_T
from anbor_types.common.annotated import ATPrice, ATDiscount
from anbor_types.warehouse.constants.constraints import (
    document_item as item_constraints,
)
from anbor_types.api.constants import DECIMAL_ZERO


class BusinessDocumentItemBaseCreateDTO(BaseModel):
    entry_id: ID_T
    price: ATPrice
    discount: ATDiscount
    count: Decimal = Field(le=item_constraints.COUNT_MAX)


class BusinessDocumentItemCreateDTO(BusinessDocumentItemBaseCreateDTO):
    variant_id: Optional[ID_T] = Field(default=None)
    expires_at: Optional[date] = Field(default=None)


class BusinessDocumentItemUpdateDTO(BaseModel):
    """One line of a full-state document update.

    ``id`` present → an existing row, ``id`` None → a new one.

    ``entry_id``, ``variant_id`` and ``expires_at`` are the line's *identity*.
    They are freely editable while the document is PENDING; on a CONFIRMED
    document they are locked and changing one is rejected, because moving a
    confirmed line onto a different entry or lot means reversing its stock and
    re-sourcing it — remove the line and add a new one instead, which the
    reconcile processors already handle.

    ``entry_id`` is required: it used to be optional and was then silently
    dropped for existing rows, so a payload could name a different entry, get a
    200, and change nothing.
    """

    id: Optional[ID_T] = None
    entry_id: ID_T
    price: ATPrice
    discount: ATDiscount
    count: Decimal = Field(le=item_constraints.COUNT_MAX)
    variant_id: Optional[ID_T] = Field(default=None)
    expires_at: Optional[date] = Field(default=None)


class ReturnDocumentItemCreateDTO(BaseModel):
    ref_item_id: ID_T
    count: Decimal = Field(le=item_constraints.COUNT_MAX, gt=DECIMAL_ZERO)


class ReturnDocumentItemUpdateDTO(BaseModel):
    """Count is the only mutable field of a return item; the item set itself is
    fixed at creation (no adding/removing via update)."""

    id: ID_T
    count: Decimal = Field(le=item_constraints.COUNT_MAX, gt=DECIMAL_ZERO)
