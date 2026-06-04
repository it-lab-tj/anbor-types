from datetime import datetime
from typing import List, Optional, Iterable

from pydantic import Field

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
    items: Iterable[TItem] = Field(
        min_length=1,
        max_length=doc_constraints.ITEM_MAX_COUNT,
    )

class SaleDocumentUpdateDTO[TItem: BusinessDocumentItemBaseUpdateDTO](
    BasePydanticModel
):
    debit_id: Optional[ID_T]
    credit_id: Optional[ID_T]
    project_id: Optional[ID_T]
    currency_id: Optional[ID_T]
    rate: Optional[ATRate]
    comment: Optional[ATComment]
    shipped_at: Optional[datetime]
    confirmed: bool = Field(default=False)
    items: Iterable[TItem] = Field(
        min_length=1,
        max_length=doc_constraints.ITEM_MAX_COUNT,
    )
