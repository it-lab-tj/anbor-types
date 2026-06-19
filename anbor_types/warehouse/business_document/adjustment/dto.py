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
from anbor_types.warehouse.constants.enums import AdjustmentDocumentKindEnum


class AdjustmentDocumentItemCreateDTO(BasePydanticModel):
    entry_id: ID_T
    price: ATPrice
    discount: ATDiscount
    count: Decimal = Field(le=item_constraints.COUNT_MAX, gt=Decimal("0"))
    variant_id: Optional[ID_T] = Field(default=None)
    expires_at: Optional[date] = Field(default=None)
    # Per-item direction; required only for HYBRID documents
    # (INVOICE or WRITE_OFF, never HYBRID itself).
    item_kind: Optional[AdjustmentDocumentKindEnum] = Field(default=None)


class AdjustmentDocumentCreateDTO(BasePydanticModel):
    storage_id: ID_T
    project_id: ID_T
    currency_id: ID_T
    rate: ATRate
    kind: AdjustmentDocumentKindEnum
    shipped_at: datetime
    confirmed: bool = Field(default=False)
    comment: Optional[ATComment] = Field(default=None)
    file_ids: Optional[ATFileIds] = Field(default=None)
    items: List[AdjustmentDocumentItemCreateDTO] = Field(
        min_length=1,
        max_length=doc_constraints.ITEM_MAX_COUNT,
    )
