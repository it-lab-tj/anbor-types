from decimal import Decimal

from pydantic import BaseModel, Field

from anbor_types import ID_T
from anbor_types.common.annotated import ATPrice, ATDiscount
from anbor_types.warehouse.constants.constraints import document_item as item_constraints


class BusinessDocumentItemCreateDTO(BaseModel):
    entry_id: ID_T
    price: ATPrice
    count: Decimal = Field(
        le=item_constraints.COUNT_MAX
    )
    discount: ATDiscount
