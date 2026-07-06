from datetime import datetime
from decimal import Decimal
from typing import List

from pydantic import Field

from anbor_types import ID_T, BasePydanticModel, Command


class CashDeskRebalanceDTO(BasePydanticModel):
    """Set a cash desk balance to an absolute target.

    The client sends the new desired balance (`target_balance`); the backend
    computes the signed delta, records an immutable rebalance-history row, and
    writes a single WalletOperation for the delta. No WalletDocument is created.
    """

    target_balance: Decimal = Field(gt=Decimal("0"))
    operating_expense_id: ID_T
    comment: str
    confirmed_at: datetime
    files_ids: List[ID_T] = Field(default_factory=list)


class CashDeskRebalanceCommand(CashDeskRebalanceDTO, Command):
    cash_desk_id: ID_T
