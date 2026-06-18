from datetime import datetime
from decimal import Decimal
from typing import List, Optional

from pydantic import Field
from anbor_types.warehouse.business_document_item.dto import (
    BusinessDocumentItemBaseCreateDTO,
)
from src.app.shared_kernel.pydantic.types import BasePydanticModel
from src.app.shared_kernel.types.base_types import ID_T
from anbor_types.common.annotated import ATRate, ATComment
from anbor_types.warehouse.constants.constraints import document as doc_constraints


class ServiceDocumentCreateDTO[TItem: BusinessDocumentItemBaseCreateDTO](
    BasePydanticModel
):
    debit_id: ID_T
    credit_id: ID_T
    project_id: ID_T
    currency_id: ID_T
    rate: ATRate
    comment: Optional[ATComment] = Field(default=None)
    shipped_at: datetime
    confirmed: bool = Field(default=False)
    items: List[TItem] = Field(
        min_length=1,
        max_length=doc_constraints.ITEM_MAX_COUNT,
    )


class ServiceOperationCreateDTO(BasePydanticModel):
    count: Decimal
    amount: Decimal
    service_id: ID_T
    company_id: ID_T
    performer_id: ID_T
    created_at: datetime
    counterparty_id: ID_T
    completed_at: datetime
