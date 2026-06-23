from datetime import datetime
from typing import List

import msgspec

from anbor_types import ID_T
from anbor_types.handbook.annotated import (
    ATPromotionEnd,
    ATPromotionName,
    ATPromotionStart,
)
from anbor_types.handbook.enums import (
    PromotionItemAwardsEnum,
    PromotionItemConditionsEnum,
)
from src.app.shared_kernel.pydantic.types import BasePydanticModel


class PromotionItemCreateDTO(BasePydanticModel):
    entry_id: ID_T
    condition: PromotionItemConditionsEnum
    award: PromotionItemAwardsEnum


class PromotionCreateDTO(BasePydanticModel):
    name: ATPromotionName
    start: ATPromotionStart
    end: ATPromotionEnd
    promotion_items: List[PromotionItemCreateDTO]


class PromotionListDTO(msgspec.Struct):
    id: ID_T
    name: str
    created_at: datetime
    start: datetime
    end: datetime
