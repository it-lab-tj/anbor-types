from datetime import date, datetime
from decimal import Decimal
from typing import List, Optional

import msgspec
from pydantic import Field

from anbor_types import BasePydanticModel, ID_T
from anbor_types.common.annotated import ATComment
from anbor_types.common.enums import StatusEnum
from anbor_types.handbook.project.dto import ProjectShortListDTO
from anbor_types.identity.user.dto import AuthorInfoShortDTO
from anbor_types.warehouse.business_document.sale.dto import (
    BusinessDocumentItemSourceDTO,
)
from anbor_types.warehouse.business_document.subject.dto import (
    SubjectForBusinessDocumentShortDataDTO,
)
from anbor_types.warehouse.business_document_item.dto import (
    BusinessDocumentItemBaseCreateDTO,
    BusinessDocumentItemUpdateDTO,
)
from anbor_types.warehouse.constants.constraints import document as doc_constraints
from anbor_types.warehouse.constants.enums import (
    BusinessDocumentApplicationStatusEnum,
)


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


class TransferDocumentUpdateDTO(BasePydanticModel):
    debit_id: ID_T
    credit_id: ID_T
    project_id: Optional[ID_T] = Field(default=None)
    comment: Optional[ATComment] = None
    shipped_at: datetime
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
    """A transfer item: the SOURCE batches it drew from (source storage) and the
    destination batch it created (destination storage)."""

    id: ID_T
    entry_id: ID_T
    price: Decimal
    discount: Decimal
    count: Decimal
    sources: List[BusinessDocumentItemSourceDTO]
    variant_id: Optional[ID_T] = None
    expires_at: Optional[date] = None
    inventory_id: Optional[ID_T] = None
    remains: Optional[Decimal] = None


class TransferDocumentDetailedDTO(msgspec.Struct):
    """Full document with items, their source batches and created inventory
    (GET_DETAILED by id)."""

    id: ID_T
    debit: SubjectForBusinessDocumentShortDataDTO
    credit: SubjectForBusinessDocumentShortDataDTO
    project: ProjectShortListDTO
    vendor_code: str
    amount: Decimal
    status: StatusEnum
    application_status: BusinessDocumentApplicationStatusEnum
    shipped_at: datetime
    created_at: datetime
    created_by: AuthorInfoShortDTO
    items: List[TransferDocumentItemDetailedDTO]
    comment: Optional[str] = None
    confirmed_at: Optional[datetime] = None
