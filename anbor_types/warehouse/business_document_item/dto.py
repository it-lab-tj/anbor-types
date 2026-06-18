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
    expires_at: Optional[date] = Field(default=None)


class BusinessDocumentItemCreateDTO(BusinessDocumentItemBaseCreateDTO):
    variant_id: Optional[ID_T] = Field(default=None)


class BusinessDocumentItemUpdateDTO(BaseModel):
    id: Optional[ID_T] = None
    price: ATPrice
    discount: ATDiscount
    count: Decimal = Field(le=item_constraints.COUNT_MAX)


class ReturnDocumentItemCreateDTO(BaseModel):
    ref_item_id: ID_T
    count: Decimal = Field(le=item_constraints.COUNT_MAX, gt=Decimal("0"))
