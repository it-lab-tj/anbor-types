from datetime import date, datetime
from decimal import Decimal
from typing import List, Optional

import msgspec
from pydantic import Field

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


class PurchaseDocumentUpdateDTO(BasePydanticModel):
    debit_id: ID_T
    credit_id: ID_T
    project_id: ID_T
    currency_id: ID_T
    rate: ATRate
    comment: Optional[ATComment] = None
    shipped_at: datetime
    confirmed: bool = Field(default=False)
    items: List[BusinessDocumentItemUpdateDTO] = Field(
        min_length=1, max_length=doc_constraints.ITEM_MAX_COUNT
    )


class PurchaseDocumentDTO(msgspec.Struct):
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


class PurchaseDocumentItemDetailedDTO(msgspec.Struct):
    """A purchase document item."""

    id: ID_T
    entry_id: ID_T
    price: Decimal
    discount: Decimal
    count: Decimal
    variant_id: Optional[ID_T] = None
    expires_at: Optional[date] = None


class PurchaseDocumentDetailedDTO(msgspec.Struct):
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
    shipped_at: datetime
    created_at: datetime
    created_by: AuthorInfoShortDTO
    paid: Decimal
    items: List[PurchaseDocumentItemDetailedDTO]
    comment: Optional[str] = None
    confirmed_at: Optional[datetime] = None
