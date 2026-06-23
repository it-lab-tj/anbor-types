from typing import List

from anbor_types import ID_T, Command
from anbor_types.handbook.promotion.dto import (
    PromotionItemCreateDTO,
    PromotionCreateDTO,
)


class PromotionCreateCommand(PromotionCreateDTO, Command): ...


class PromotionItemsSetCommand(Command):
    promotion_id: ID_T
    promotion_items: List[PromotionItemCreateDTO]
