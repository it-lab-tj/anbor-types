from typing import List, Optional


from anbor_types import ID_T, BasePydanticModel
from anbor_types.common.annotated import ATComment, ATFileIds
from pydantic import Field

from anbor_types.warehouse.business_document_item.dto import (
    ReturnDocumentItemCreateDTO,
    ReturnDocumentItemUpdateDTO,
)
from anbor_types.warehouse.constants.constraints import document as doc_constraints
from anbor_types.utils.functions import get_now_utc
from anbor_types.common.annotated import ATDatetimeDefault


class ReturnOutBusinessDocumentCreateDTO(BasePydanticModel):
    business_document_id: ID_T = Field()
    shipped_at: ATDatetimeDefault = Field(default_factory=get_now_utc)
    items: List[ReturnDocumentItemCreateDTO] = Field(
        max_length=doc_constraints.ITEM_MAX_COUNT
    )
    confirmed: bool = Field(default=False)
    comment: Optional[ATComment] = Field(default=None)
    file_ids: Optional[ATFileIds] = Field(default=None)
    tag_id: Optional[ID_T] = None


class ReturnOutBusinessDocumentUpdateDTO(BasePydanticModel):
    """Count-only update: items may be a subset of the document's items
    (omitted items stay unchanged); everything else about the return —
    shipped_at, referenced purchase, item set — is immutable."""

    items: List[ReturnDocumentItemUpdateDTO] = Field(
        min_length=1, max_length=doc_constraints.ITEM_MAX_COUNT
    )
    comment: Optional[ATComment] = Field(default=None)
    file_ids: Optional[ATFileIds] = Field(default=None)
