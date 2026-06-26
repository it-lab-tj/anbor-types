from datetime import datetime
from decimal import Decimal

from anbor_types import ID_T, BasePydanticModel
from anbor_types.common.enums import ContentTypeEnum


class WalletOperationCreateDTO(BasePydanticModel):
    amount: Decimal
    content_id: ID_T
    content_type: ContentTypeEnum
    cash_desk_id: ID_T
    confirmed_at: datetime
