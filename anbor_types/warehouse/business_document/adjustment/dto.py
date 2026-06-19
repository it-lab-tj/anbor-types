from datetime import date, datetime
from decimal import Decimal
from typing import List, Optional

from pydantic import Field

from anbor_types import BasePydanticModel, ID_T
from anbor_types.common.annotated import (
    ATComment,
    ATDiscount,
    ATFileIds,
    ATPrice,
    ATRate,
)
from anbor_types.warehouse.constants.constraints import document as doc_constraints
from anbor_types.warehouse.constants.constraints import (
    document_item as item_constraints,
)
from anbor_types.warehouse.constants.enums import (
    AdjustmentDocumentKindEnum,
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
