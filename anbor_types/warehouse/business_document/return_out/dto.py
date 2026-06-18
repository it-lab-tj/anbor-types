from datetime import datetime
from typing import List, Optional

from anbor_types.common.annotated import ATComment, ATFileIds
from pydantic import Field

from anbor_types.warehouse.business_document_item.dto import ReturnDocumentItemCreateDTO
from anbor_types.warehouse.constants.constraints import document as doc_constraints
from src.app.shared_kernel.pydantic.types import BasePydanticModel
from src.app.shared_kernel.types.base_types import ID_T


class ReturnOutBusinessDocumentCreateDTO(BasePydanticModel):
    business_document_id: ID_T = Field()
    shipped_at: datetime
    items: List[ReturnDocumentItemCreateDTO] = Field(
        max_length=doc_constraints.ITEM_MAX_COUNT
    )
    confirmed: bool = Field(default=False)
    comment: Optional[ATComment] = Field(default=None)
    file_ids: Optional[ATFileIds] = Field(default=None)
