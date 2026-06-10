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


class BusinessDocumentItemBaseUpdateDTO(BaseModel):
    id: Optional[ID_T] = None
    entry_id: ID_T
    price: ATPrice
    discount: ATDiscount
    count: Decimal = Field(le=item_constraints.COUNT_MAX)
    performer_id: Optional[ID_T] = Field(default=None)
    expires_at: Optional[date] = Field(default=None)


class BusinessDocumentItemUpdateDTO(BusinessDocumentItemBaseUpdateDTO):
    variant_id: Optional[ID_T] = Field(default=None)
