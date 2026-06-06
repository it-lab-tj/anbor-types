from datetime import datetime
from typing import List, Optional

from pydantic import Field

from anbor_types import BasePydanticModel, ID_T
from anbor_types.common.annotated import ATComment
from anbor_types.warehouse.business_document_item.dto import (
    BusinessDocumentItemBaseCreateDTO,
)
from anbor_types.warehouse.constants.constraints import document as doc_constraints


class TransferDocumentCreateDTO[TItem: BusinessDocumentItemBaseCreateDTO](
    BasePydanticModel
):
    debit_id: ID_T
    credit_id: ID_T
    project_id: Optional[ID_T] = Field(default=None)
    comment: Optional[ATComment] = Field(default=None)
    shipped_at: datetime
    confirmed: bool = Field(default=False)
    items: List[TItem] = Field(
        min_length=1,
        max_length=doc_constraints.ITEM_MAX_COUNT,
    )
