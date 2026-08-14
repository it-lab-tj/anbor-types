from datetime import date, datetime
from decimal import Decimal
from typing import List, Optional

from anbor_types.catalog.catalog_entry.dto import CatalogEntryOnBusinessDocumentItemDTO
from anbor_types.catalog.category.dto import CharacteristicValuePairDTO
from anbor_types.common.dto import FileShortDTO
from anbor_types.common.enums import StatusEnum
from anbor_types.warehouse.constants.enums import (
    BusinessDocumentActionEnum,
    BusinessDocumentApplicationStatusEnum,
)

import msgspec
from pydantic import Field

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

from anbor_types import BasePydanticModel, ID_T
from anbor_types.common.annotated import ATDatetime, ATFileIds, ATRate, ATComment


class SaleDocumentCreateDTO[TItem: BusinessDocumentItemBaseCreateDTO](
    BasePydanticModel
):
    debit_id: ID_T
    credit_id: ID_T
    project_id: ID_T
    currency_id: ID_T
    rate: ATRate
    comment: Optional[ATComment] = Field(default=None)
    shipped_at: ATDatetime
    file_ids: Optional[ATFileIds] = Field(default=None)
    confirmed: bool = Field(default=False)
    items: List[TItem] = Field(
        min_length=1,
        max_length=doc_constraints.ITEM_MAX_COUNT,
    )


class SaleDocumentUpdateDTO(BasePydanticModel):
    debit_id: ID_T
    project_id: ID_T
    currency_id: ID_T
    rate: ATRate
    comment: Optional[ATComment] = None
    confirmed: bool = Field(default=False)
    items: List[BusinessDocumentItemUpdateDTO] = Field(
        min_length=1, max_length=doc_constraints.ITEM_MAX_COUNT
    )


class SaleDocumentListDTO(msgspec.Struct):
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
    created_at: datetime
    created_by: AuthorInfoShortDTO
    paid: Decimal


class SaleDocumentWithProfitListDTO(SaleDocumentListDTO):
    profit: Decimal


class SaleDocumentDTO(msgspec.Struct):
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


class BusinessDocumentItemSourceDTO(msgspec.Struct):
    """One SOURCE extension: the inventory an outgoing item was drawn from."""

    inventory_id: ID_T
    count: Decimal
    rank: int


class SaleDocumentItemBaseDetailedDTO(msgspec.Struct):
    id: ID_T
    entry: CatalogEntryOnBusinessDocumentItemDTO
    price: Decimal
    discount: Decimal
    count: Decimal


class SaleDocumentItemDetailedDTO(SaleDocumentItemBaseDetailedDTO):
    variant_id: Optional[ID_T] = None
    expires_at: Optional[date] = None
    # The variant's characteristics, resolved to names. Empty when the item
    # carries no variant.
    characteristic_values: List[CharacteristicValuePairDTO] = msgspec.field(
        default_factory=list
    )


class SaleDocumentItemListProfitDTO(SaleDocumentItemBaseDetailedDTO):
    profit: Decimal
    variant_id: Optional[ID_T] = None
    expires_at: Optional[date] = None


class SaleDocumentBaseDetailedDTO(msgspec.Struct):
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
    files: List[FileShortDTO]
    paid: Decimal
    # «Сумма прописью» — `amount` written out in Russian words, built with
    # `numeric_funcs.get_capstone` at the repository. Printed on documents.
    capstone: str


class SaleDocumentProfitDetailedDto(SaleDocumentBaseDetailedDTO):
    items: List[SaleDocumentItemListProfitDTO]
    comment: Optional[str] = None
    confirmed_at: Optional[datetime] = None


class SaleDocumentDetailedDTO(SaleDocumentBaseDetailedDTO):
    items: List[SaleDocumentItemDetailedDTO]
    comment: Optional[str] = None
    confirmed_at: Optional[datetime] = None


class SaleProfitDTO(msgspec.Struct):
    """Scalar profit result of `POST /warehouse/sale/profit`."""

    profit: Decimal
