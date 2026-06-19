from datetime import datetime
from typing import List, Optional

from pydantic import Field

from anbor_types.warehouse.business_document_item.dto import (
    BusinessDocumentItemBaseCreateDTO,
)
from anbor_types.warehouse.constants.constraints import document as doc_constraints

from anbor_types import BasePydanticModel, ID_T
from anbor_types.common.annotated import ATRate, ATComment, ATFileIds


class PurchaseDocumentCreateDTO[TItem: BusinessDocumentItemBaseCreateDTO](
    BasePydanticModel
):
    debit_id: ID_T
    credit_id: ID_T
    project_id: ID_T
    currency_id: ID_T
    rate: ATRate
    shipped_at: datetime
    confirmed: bool = Field(default=False)
    comment: Optional[ATComment] = Field(default=None)
    file_ids: Optional[ATFileIds] = Field(default=None)
    items: List[TItem] = Field(
        min_length=1,
        max_length=doc_constraints.ITEM_MAX_COUNT,
    )
