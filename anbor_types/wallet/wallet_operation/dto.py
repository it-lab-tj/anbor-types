from decimal import Decimal
from typing import Optional

from anbor_types import ID_T, BasePydanticModel
from anbor_types.common.annotated import ATDatetime
from anbor_types.common.enums import ContentTypeEnum


class WalletOperationCreateDTO(BasePydanticModel):
    amount: Decimal
    content_id: Optional[ID_T] = None
    content_type: Optional[ContentTypeEnum] = None
    confirmed_at: ATDatetime
    cash_desk_id: Optional[ID_T] = None
