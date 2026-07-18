from typing import List, Optional

from anbor_types.common.annotated import ATComment, ATDatetime, ATFileIds
from pydantic import Field

from anbor_types import BasePydanticModel, ID_T
from anbor_types.warehouse.business_document_item.dto import (
    ReturnDocumentItemCreateDTO,
    ReturnDocumentItemUpdateDTO,
)

from anbor_types.warehouse.constants.constraints import document as doc_constraints


class ReturnInBusinessDocumentCreateDTO(BasePydanticModel):
    business_document_id: ID_T = Field()
    shipped_at: ATDatetime
    items: List[ReturnDocumentItemCreateDTO] = Field(
        max_length=doc_constraints.ITEM_MAX_COUNT
    )
    confirmed: bool = Field(default=False)
    comment: Optional[ATComment] = Field(default=None)
    file_ids: Optional[ATFileIds] = Field(default=None)


class ReturnInBusinessDocumentUpdateDTO(BasePydanticModel):
    """Count-only update: items may be a subset of the document's items
    (omitted items stay unchanged); everything else about the return —
    shipped_at, referenced sale, item set — is immutable."""

    items: List[ReturnDocumentItemUpdateDTO] = Field(
        min_length=1, max_length=doc_constraints.ITEM_MAX_COUNT
    )
    comment: Optional[ATComment] = Field(default=None)
    file_ids: Optional[ATFileIds] = Field(default=None)
