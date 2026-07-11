from datetime import datetime
from decimal import Decimal
from typing import Optional

from anbor_types import ID_T, BasePydanticModel
from anbor_types.common.enums import ContentTypeEnum


class WalletOperationCreateDTO(BasePydanticModel):
    amount: Decimal
    content_id: ID_T
    content_type: ContentTypeEnum
    confirmed_at: datetime
    cash_desk_id: Optional[ID_T] = None
