from datetime import date
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, Field

from anbor_types import ID_T
from anbor_types.common.annotated import ATPrice, ATDiscount
from anbor_types.warehouse.constants.constraints import (
    document_item as item_constraints,
)


class BusinessDocumentItemBaseCreateDTO(BaseModel):
    entry_id: ID_T
    price: ATPrice
    discount: ATDiscount
    count: Decimal = Field(le=item_constraints.COUNT_MAX)


class BusinessDocumentItemCreateDTO(BusinessDocumentItemBaseCreateDTO):
    variant_id: Optional[ID_T] = Field(default=None)
    expires_at: Optional[date] = Field(default=None)


class BusinessDocumentItemUpdateDTO(BaseModel):
    id: Optional[ID_T] = None
    price: ATPrice
    discount: ATDiscount
    count: Decimal = Field(le=item_constraints.COUNT_MAX)


class ReturnDocumentItemCreateDTO(BaseModel):
    ref_item_id: ID_T
    count: Decimal = Field(le=item_constraints.COUNT_MAX, gt=Decimal("0"))


class ReturnDocumentItemUpdateDTO(BaseModel):
    """Count is the only mutable field of a return item; the item set itself is
    fixed at creation (no adding/removing via update)."""

    id: ID_T
    count: Decimal = Field(le=item_constraints.COUNT_MAX, gt=Decimal("0"))
