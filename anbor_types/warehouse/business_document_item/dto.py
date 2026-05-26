from decimal import Decimal
from typing import List, Optional

from pydantic import BaseModel, Field

from anbor_types import ID_T
from anbor_types.common.annotated import ATPrice, ATDiscount
from anbor_types.warehouse.constants.constraints import (
    document_item as item_constraints,
)

class BusinessDocumentItemBaseCreateDTO(BaseModel):
    entry_id: ID_T
    price: ATPrice
    count: Decimal = Field(le=item_constraints.COUNT_MAX)
    discount: ATDiscount

class BusinessDocumentItemCreateDTO(BusinessDocumentItemBaseCreateDTO):
    variant_id: Optional[ID_T] = Field(default=None)
