from datetime import date, datetime
from decimal import Decimal
from typing import List, Optional

import msgspec
from pydantic import Field

from anbor_types import BasePydanticModel, ID_T
from anbor_types.common.annotated import (
    ATComment,
    ATDiscount,
    ATFileIds,
    ATPrice,
    ATRate,
)
from anbor_types.common.enums import StatusEnum
from anbor_types.handbook.project.dto import ProjectShortListDTO
from anbor_types.identity.user.dto import AuthorInfoShortDTO
from anbor_types.warehouse.business_document.sale.dto import (
    BusinessDocumentItemSourceDTO,
)
from anbor_types.warehouse.business_document.subject.dto import (
    SubjectForBusinessDocumentShortDataDTO,
)
from anbor_types.warehouse.constants.constraints import document as doc_constraints
from anbor_types.warehouse.constants.constraints import (
    document_item as item_constraints,
)
from anbor_types.warehouse.constants.enums import (
    AdjustmentDocumentKindEnum,
    BusinessDocumentApplicationStatusEnum,
    BusinessDocumentItemKindEnum,
)


class AdjustmentDocumentItemBaseCreateDTO(BasePydanticModel):
    entry_id: ID_T
    price: ATPrice
    discount: ATDiscount
    kind: BusinessDocumentItemKindEnum = Field(
        description="Направление движения товара: 1=INCOME (поступление), 2=OUTCOME (списание)."
    )
    count: Decimal = Field(le=item_constraints.COUNT_MAX, gt=Decimal("0"))
    expires_at: Optional[date] = Field(default=None)


class AdjustmentDocumentCreateDTO[TItem: AdjustmentDocumentItemBaseCreateDTO](
    BasePydanticModel
):
    storage_id: ID_T
    project_id: ID_T
    currency_id: ID_T
    rate: ATRate
    shipped_at: datetime
    kind: AdjustmentDocumentKindEnum = Field(
        description=(
            "Вид документа: 0=WRITE_OFF (все строки OUTCOME), "
            "1=INVOICE (все строки INCOME), "
            "2=HYBRID (строки содержат оба типа). "
            "Должен соответствовать видам строк."
        )
    )
    confirmed: bool = Field(default=False)
    comment: Optional[ATComment] = Field(default=None)
    file_ids: Optional[ATFileIds] = Field(default=None)
    items: List[TItem] = Field(
        min_length=1,
        max_length=doc_constraints.ITEM_MAX_COUNT,
    )


class AdjustmentDocumentItemUpdateDTO(BasePydanticModel):
    """An item on an update: ``id`` present → existing row, ``id`` None → new row.
    ``kind`` (1=INCOME, 2=OUTCOME) is carried per item, like the create item."""

    id: Optional[ID_T] = Field(default=None)
    entry_id: ID_T
    price: ATPrice
    discount: ATDiscount
    kind: BusinessDocumentItemKindEnum
    count: Decimal = Field(le=item_constraints.COUNT_MAX, gt=Decimal("0"))
    variant_id: Optional[ID_T] = Field(default=None)
    expires_at: Optional[date] = Field(default=None)


class AdjustmentDocumentUpdateDTO(BasePydanticModel):
    # ``storage_id`` and ``shipped_at`` are intentionally absent: a document's
    # storage and date are immutable after creation.
    project_id: ID_T
    currency_id: ID_T
    rate: ATRate
    kind: AdjustmentDocumentKindEnum
    confirmed: bool = Field(default=False)
    comment: Optional[ATComment] = Field(default=None)
    file_ids: Optional[ATFileIds] = Field(default=None)
    items: List[AdjustmentDocumentItemUpdateDTO] = Field(
        min_length=1,
        max_length=doc_constraints.ITEM_MAX_COUNT,
    )


class AdjustmentDocumentDTO(msgspec.Struct):
    """Single-document summary (GET by id)."""

    id: ID_T
    storage: SubjectForBusinessDocumentShortDataDTO
    project: ProjectShortListDTO
    vendor_code: str
    kind: AdjustmentDocumentKindEnum
    count_items: int
    amount: Decimal
    status: StatusEnum
    application_status: BusinessDocumentApplicationStatusEnum
    shipped_at: datetime
    created_at: datetime
    created_by: AuthorInfoShortDTO
    comment: Optional[str] = None
    confirmed_at: Optional[datetime] = None


class AdjustmentDocumentItemDetailedDTO(msgspec.Struct):
    """An adjustment item. INCOME items created a destination batch
    (``inventory_id``/``remains``); OUTCOME items drew SOURCE batches
    (``sources``). The irrelevant side is empty/None for the given ``kind``."""

    id: ID_T
    entry_id: ID_T
    price: Decimal
    discount: Decimal
    count: Decimal
    kind: BusinessDocumentItemKindEnum
    sources: List[BusinessDocumentItemSourceDTO]
    variant_id: Optional[ID_T] = None
    expires_at: Optional[date] = None
    inventory_id: Optional[ID_T] = None
    remains: Optional[Decimal] = None


class AdjustmentDocumentDetailedDTO(msgspec.Struct):
    """Full document with items, their SOURCE batches (OUTCOME) and created
    inventory (INCOME) — GET_DETAILED by id."""

    id: ID_T
    storage: SubjectForBusinessDocumentShortDataDTO
    project: ProjectShortListDTO
    vendor_code: str
    kind: AdjustmentDocumentKindEnum
    amount: Decimal
    status: StatusEnum
    application_status: BusinessDocumentApplicationStatusEnum
    shipped_at: datetime
    created_at: datetime
    created_by: AuthorInfoShortDTO
    items: List[AdjustmentDocumentItemDetailedDTO]
    comment: Optional[str] = None
    confirmed_at: Optional[datetime] = None
