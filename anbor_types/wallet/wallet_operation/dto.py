from decimal import Decimal

from pydantic import Field

from anbor_types import ID_T, BasePydanticModel
from anbor_types.common.enums import ContentTypeEnum
from anbor_types.common.annotated import ATDatetimeDefault
from anbor_types.utils.functions import get_now_utc


class WalletOperationCreateDTO(BasePydanticModel):
    """One ledger row: who the balance belongs to, how much, when.

    The ledger carries no notion of the action that produced the row -- no
    document kind, no direction, no second operand. `content_type`/`content_id`
    name the OWNER of the affected balance and nothing else, uniformly, so a
    balance is `SUM(amount)` over the rows naming that owner. A document that
    moves two balances posts two of these.
    """

    content_type: ContentTypeEnum
    content_id: ID_T
    amount: Decimal
    confirmed_at: ATDatetimeDefault = Field(default_factory=get_now_utc)
