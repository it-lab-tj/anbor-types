from datetime import datetime
from decimal import Decimal
from typing import List, Optional

import msgspec
from pydantic import Field

from anbor_types import ID_T, BasePydanticModel
from anbor_types.common.annotated import ATComment, ATDatetime, ATFileIds, ATRate
from anbor_types.catalog.catalog_entry.dto import (
    CatalogEntryOnBusinessDocumentItemDTO,
)
from anbor_types.common.dto import FileShortDTO, NameIdDTO
from anbor_types.common.enums import StatusEnum
from anbor_types.handbook.project.dto import ProjectShortListDTO
from anbor_types.identity.user.dto import AuthorInfoShortDTO
from anbor_types.wallet.currency.dto import CurrencyShortListDTO
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


class ServiceDocumentCreateDTO[TItem: BusinessDocumentItemBaseCreateDTO](
    BasePydanticModel
):
    # debit -> counterparty (billed), credit -> performer (executor)
    debit_id: ID_T
    credit_id: ID_T
    project_id: ID_T
    currency_id: ID_T
    rate: ATRate
    file_ids: Optional[ATFileIds] = Field(default=None)
    tag_id: Optional[ID_T] = None
    comment: Optional[ATComment] = Field(default=None)
    shipped_at: ATDatetime
    confirmed: bool = Field(default=False)
    items: List[TItem] = Field(
        min_length=1,
        max_length=doc_constraints.ITEM_MAX_COUNT,
    )


class ServiceDocumentUpdateDTO(BasePydanticModel):
    debit_id: ID_T
    credit_id: ID_T
    project_id: ID_T
    currency_id: ID_T
    rate: ATRate
    comment: Optional[ATComment] = None
    shipped_at: ATDatetime
    confirmed: bool = Field(default=False)
    items: List[BusinessDocumentItemUpdateDTO] = Field(
        min_length=1, max_length=doc_constraints.ITEM_MAX_COUNT
    )


class ServiceShortDTO(msgspec.Struct):
    id: ID_T
    name: str
    selling_price: Decimal


class ServiceDocumentListDTO(msgspec.Struct):
    id: ID_T
    debit: SubjectForBusinessDocumentShortDataDTO
    credit: SubjectForBusinessDocumentShortDataDTO
    project: ProjectShortListDTO
    currency: CurrencyShortListDTO
    rate: Decimal
    vendor_code: str
    count_items: int
    amount: Decimal
    status: StatusEnum
    tag: NameIdDTO
    created_at: datetime
    created_by: AuthorInfoShortDTO
    paid: Decimal


class ServiceDocumentDTO(msgspec.Struct):
    """Single-document summary (GET by id)."""

    id: ID_T
    debit: SubjectForBusinessDocumentShortDataDTO
    credit: SubjectForBusinessDocumentShortDataDTO
    project: ProjectShortListDTO
    currency: CurrencyShortListDTO
    rate: Decimal
    vendor_code: str
    count_items: int
    amount: Decimal
    status: StatusEnum
    application_status: BusinessDocumentApplicationStatusEnum
    shipped_at: datetime
    created_at: datetime
    created_by: AuthorInfoShortDTO
    paid: Decimal
    comment: Optional[str] = None
    confirmed_at: Optional[datetime] = None


class ServiceDocumentItemDetailedDTO(msgspec.Struct):
    """One service line item. Services carry no stock, hence no sources."""

    id: ID_T
    entry: CatalogEntryOnBusinessDocumentItemDTO
    price: Decimal
    discount: Decimal
    count: Decimal


class ServiceDocumentDetailedDTO(msgspec.Struct):
    """Full document with its items (GET_DETAILED by id)."""

    id: ID_T
    action: BusinessDocumentActionEnum
    debit: SubjectForBusinessDocumentShortDataDTO
    credit: SubjectForBusinessDocumentShortDataDTO
    project: ProjectShortListDTO
    currency: CurrencyShortListDTO
    rate: Decimal
    vendor_code: str
    amount: Decimal
    status: StatusEnum
    application_status: BusinessDocumentApplicationStatusEnum
    files: List[FileShortDTO]
    shipped_at: datetime
    created_at: datetime
    created_by: AuthorInfoShortDTO
    tag: NameIdDTO
    paid: Decimal
    items: List[ServiceDocumentItemDetailedDTO]
    # «Сумма прописью» — `amount` written out in Russian words, built with
    # `numeric_funcs.get_capstone` at the repository. Printed on documents.
    capstone: str
    comment: Optional[str] = None
    confirmed_at: Optional[datetime] = None


class ServiceOperationCreateDTO(BasePydanticModel):
    count: Decimal
    amount: Decimal
    service_id: ID_T
    performer_id: ID_T
    document_item_id: ID_T
    created_at: ATDatetime
    counterparty_id: ID_T
    completed_at: ATDatetime
