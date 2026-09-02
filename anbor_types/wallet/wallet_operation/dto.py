from decimal import Decimal
from typing import Optional

from pydantic import Field

from anbor_types import ID_T, BasePydanticModel
from anbor_types.common.enums import ContentTypeEnum
from anbor_types.common.annotated import ATDatetimeDefault
from anbor_types.utils.functions import get_now_utc


class WalletOperationCreateDTO(BasePydanticModel):
    amount: Decimal
    content_id: Optional[ID_T] = None
    content_type: Optional[ContentTypeEnum] = None
    confirmed_at: ATDatetimeDefault = Field(default_factory=get_now_utc)
    cash_desk_id: Optional[ID_T] = None
