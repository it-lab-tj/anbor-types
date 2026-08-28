from datetime import date, datetime
from decimal import Decimal
from typing import List, Optional

import msgspec
from pydantic import Field

from anbor_types import BasePydanticModel, ID_T
from anbor_types.common.annotated import ATComment, ATDatetime, ATFileIds
from anbor_types.catalog.catalog_entry.dto import (
    CatalogEntryOnBusinessDocumentItemDTO,
)
from anbor_types.catalog.category.dto import CharacteristicValuePairDTO
from anbor_types.common.dto import FileShortDTO
from anbor_types.common.enums import StatusEnum
from anbor_types.handbook.project.dto import ProjectShortListDTO
from anbor_types.identity.user.dto import AuthorInfoShortDTO
from anbor_types.warehouse.business_document.subject.dto import (
    SubjectForBusinessDocumentShortDataDTO,
)
from anbor_types.warehouse.business_document_item.dto import (
    BusinessDocumentItemBaseCreateDTO,
    BusinessDocumentItemUpdateDTO,
)
from anbor_types.warehouse.constants.constraints import document as doc_constraints
from anbor_types.warehouse.constants.enums import (
    BusinessDocumentActionEnum,
    BusinessDocumentApplicationStatusEnum,
)


class TransferDocumentCreateDTO[TItem: BusinessDocumentItemBaseCreateDTO](
    BasePydanticModel
):
    debit_id: ID_T
    credit_id: ID_T
    project_id: Optional[ID_T] = Field(default=None)
    comment: Optional[ATComment] = Field(default=None)
    shipped_at: ATDatetime
    confirmed: bool = Field(default=False)
    file_ids: Optional[ATFileIds] = Field(default=None)
    tag_id: Optional[ID_T] = None
    items: List[TItem] = Field(
        min_length=1,
        max_length=doc_constraints.ITEM_MAX_COUNT,
    )


class TransferDocumentUpdateDTO(BasePydanticModel):
    debit_id: ID_T
    credit_id: ID_T
    project_id: Optional[ID_T] = Field(default=None)
    comment: Optional[ATComment] = None
    shipped_at: ATDatetime
    confirmed: bool = Field(default=False)
    items: List[BusinessDocumentItemUpdateDTO] = Field(
        min_length=1, max_length=doc_constraints.ITEM_MAX_COUNT
    )


class TransferDocumentDTO(msgspec.Struct):
    """Single-document summary (GET by id)."""

    id: ID_T
    debit: SubjectForBusinessDocumentShortDataDTO
    credit: SubjectForBusinessDocumentShortDataDTO
    project: ProjectShortListDTO
    vendor_code: str
    count_items: int
    amount: Decimal
    status: StatusEnum
    application_status: BusinessDocumentApplicationStatusEnum
    shipped_at: datetime
    created_at: datetime
    created_by: AuthorInfoShortDTO
    comment: Optional[str] = None
    confirmed_at: Optional[datetime] = None


class TransferDocumentItemDetailedDTO(msgspec.Struct):
    """A transfer document item."""

    id: ID_T
    entry: CatalogEntryOnBusinessDocumentItemDTO
    price: Decimal
    discount: Decimal
    count: Decimal
    variant_id: Optional[ID_T] = None
    expires_at: Optional[date] = None
    # The variant's characteristics, resolved to names. Empty when the item
    # carries no variant.
    characteristic_values: List[CharacteristicValuePairDTO] = msgspec.field(
        default_factory=list
    )


class TransferDocumentDetailedDTO(msgspec.Struct):
    """Full document with its items (GET_DETAILED by id)."""

    id: ID_T
    action: BusinessDocumentActionEnum
    debit: SubjectForBusinessDocumentShortDataDTO
    credit: SubjectForBusinessDocumentShortDataDTO
    project: ProjectShortListDTO
    vendor_code: str
    amount: Decimal
    status: StatusEnum
    application_status: BusinessDocumentApplicationStatusEnum
    files: List[FileShortDTO]
    shipped_at: datetime
    created_at: datetime
    created_by: AuthorInfoShortDTO
    items: List[TransferDocumentItemDetailedDTO]
    # «Сумма прописью» — `amount` in words. A transfer carries no
    # currency (storage/0052 leaves it NULL), so no unit is named.
    capstone: str
    comment: Optional[str] = None
    confirmed_at: Optional[datetime] = None
