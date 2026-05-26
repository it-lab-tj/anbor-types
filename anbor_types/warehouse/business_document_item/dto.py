from decimal import Decimal
from typing import List

from pydantic import BaseModel, Field

from anbor_types import ID_T
from anbor_types.catalog.category.dto import CharValuePairDTO
from anbor_types.common.annotated import ATPrice, ATDiscount
from anbor_types.warehouse.constants.constraints import (
    document_item as item_constraints,
)
from anbor_types.warehouse.constants.constraints import document_item as item_constraints


class BusinessDocumentItemCreateDTO(BaseModel):
    entry_id: ID_T
    price: ATPrice
    count: Decimal = Field(le=item_constraints.COUNT_MAX)
    discount: ATDiscount
    char_values: List[CharValuePairDTO] = Field(
        default_factory=list,
        max_length=item_constraints.CHAR_VALUES_MAX_COUNT,
    )
