from datetime import datetime
from typing import List

from pydantic import Field

from anbor_types import BasePydanticModel, ID_T
from anbor_types.common.annotated import ATRate, ATComment
from anbor_types.warehouse.business_document_item.dto import BusinessDocumentItemCreateDTO
from anbor_types.warehouse.constants.constraints import document as doc_constraints



class PurchaseDocumentCreateDTO(BasePydanticModel):
    debit_id: ID_T
    credit_id: ID_T
    project_id: ID_T
    currency_id: ID_T
    rate: ATRate
    comment: ATComment
    shipped_at: datetime
    items: List[BusinessDocumentItemCreateDTO] = Field(min_length=1, max_length=doc_constraints.ITEM_MAX_COUNT)
