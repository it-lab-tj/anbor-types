from datetime import datetime
from decimal import Decimal
from typing import List, Optional
from anbor_types.common.enums import StatusEnum

import msgspec
from pydantic import Field

from anbor_types.handbook.project.dto import ProjectShortListDTO
from anbor_types.identity.user.dto import AuthorInfoShortDTO
from anbor_types.wallet.currency.dto import CurrenctShortListDTO
from anbor_types.warehouse.business_document.subject.dto import (
    SubjectForBusinessDocumentShortDataDTO,
)
from anbor_types.warehouse.business_document_item.dto import (
    BusinessDocumentItemBaseCreateDTO,
    BusinessDocumentItemBaseUpdateDTO,
)
from anbor_types.warehouse.constants.constraints import document as doc_constraints

from anbor_types import BasePydanticModel, ID_T
from anbor_types.common.annotated import ATRate, ATComment


class SaleDocumentCreateDTO[TItem: BusinessDocumentItemBaseCreateDTO](
    BasePydanticModel
):
    debit_id: ID_T
    credit_id: ID_T
    project_id: ID_T
    currency_id: ID_T
    rate: ATRate
    comment: ATComment
    shipped_at: datetime
    confirmed: bool = Field(default=False)
    items: List[TItem] = Field(
        min_length=1,
        max_length=doc_constraints.ITEM_MAX_COUNT,
    )


class SaleDocumentUpdateDTO[TItem: BusinessDocumentItemBaseUpdateDTO](
    BasePydanticModel
):
    debit_id: Optional[ID_T] = None
    credit_id: Optional[ID_T] = None
    project_id: Optional[ID_T] = None
    currency_id: Optional[ID_T] = None
    rate: Optional[ATRate] = None
    comment: Optional[ATComment] = None
    shipped_at: Optional[datetime] = None
    confirmed: bool = Field(default=False)
    items: List[TItem] = Field(
        min_length=0, max_length=doc_constraints.ITEM_MAX_COUNT, default=None
    )


class SaleDocumentListDTO(msgspec.Struct):
    id: ID_T
    debit: SubjectForBusinessDocumentShortDataDTO
    credit: SubjectForBusinessDocumentShortDataDTO
    project: ProjectShortListDTO
    currency: CurrenctShortListDTO
    rate: Decimal
    vendor_code: str
    count_items: int
    amount: Decimal
    status: StatusEnum
    created_at: datetime
    created_by: AuthorInfoShortDTO
    paid: Decimal
