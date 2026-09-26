from datetime import date
from decimal import Decimal
from typing import List, Optional

import msgspec
from pydantic import BaseModel, Field

from anbor_types import ID_T, BasePydanticModel
from anbor_types.catalog.category.dto import CharValueDTO
from anbor_types.common.annotated import ATPrice, ATDiscount
from anbor_types.common.dto import NameIdDTO
from anbor_types.warehouse.constants.constraints import (
    document_item as item_constraints,
)
from anbor_types.api.constants import DECIMAL_ZERO
from anbor_types.warehouse.constants.enums import BusinessDocumentItemKindEnum


class BusinessDocumentItemBaseCreateDTO(BaseModel):
    entry_id: ID_T
    price: ATPrice
    discount: ATDiscount
    count: Decimal = Field(le=item_constraints.COUNT_MAX)


class BusinessDocumentItemCreateDTO(BusinessDocumentItemBaseCreateDTO):
    expires_at: Optional[date] = Field(default=None)


class BusinessDocumentItemBaseUpdateDTO(BasePydanticModel):
    """What every action's update line carries, and the bound the document
    update DTOs are generic over — the mirror of
    ``BusinessDocumentItemBaseCreateDTO`` on the write-back side.

    ``id`` present → an existing row, ``id`` None → a new one.

    ``entry_id``, the variant ``char_values`` resolve to, and ``expires_at`` are
    the line's *identity*. They are freely editable while the document is
    PENDING; on a CONFIRMED document they are locked and changing one is
    rejected, because moving a confirmed line onto a different entry or lot
    means reversing its stock and re-sourcing it — remove the line and add a new
    one instead, which the reconcile processors already handle.

    ``entry_id`` is required: it used to be optional and was then silently
    dropped for existing rows, so a payload could name a different entry, get a
    200, and change nothing.

    ``char_values`` names the characteristics of the line, exactly as on create.
    The server resolves them to a catalog entry variant; the variant id itself
    is internal and is neither accepted nor needed here. Full-state, like every
    other field: an empty list means the line has no characteristics, so a line
    that had a variant loses it. Send back what the detailed GET returned under
    ``characteristics`` to leave a line unchanged.
    """

    id: Optional[ID_T] = None
    entry_id: ID_T
    price: ATPrice
    discount: ATDiscount
    count: Decimal = Field(le=item_constraints.COUNT_MAX)
    expires_at: Optional[date] = Field(default=None)
    char_values: List[CharValueDTO] = Field(
        default_factory=list,
        max_length=item_constraints.CHAR_VALUES_MAX_COUNT,
    )


class BusinessDocumentItemShortDTO(msgspec.Struct):
    id: ID_T
    entry: NameIdDTO
    kind: BusinessDocumentItemKindEnum


class BusinessDocumentItemUpdateDTO(BusinessDocumentItemBaseUpdateDTO):
    """The update line of every action whose items carry nothing of their own
    (sale, purchase, transfer, service). Adjustment declares its own."""


class ReturnDocumentItemCreateDTO(BaseModel):
    ref_item_id: ID_T
    count: Decimal = Field(le=item_constraints.COUNT_MAX, gt=DECIMAL_ZERO)


class ReturnDocumentItemUpdateDTO(BaseModel):
    """Count is the only mutable field of a return item; the item set itself is
    fixed at creation (no adding/removing via update)."""

    id: ID_T
    count: Decimal = Field(le=item_constraints.COUNT_MAX, gt=DECIMAL_ZERO)
