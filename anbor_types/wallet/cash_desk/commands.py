from decimal import Decimal
from typing import List

from pydantic import Field

from anbor_types import ID_T, BasePydanticModel, Command
from anbor_types.common.annotated import ATDatetime
from anbor_types.wallet.cash_desk.constraints import CASH_DESK_TITLE_MAX_LENGTH


class CashDeskCreateDTO(BasePydanticModel):
    title: str = Field(min_length=1, max_length=CASH_DESK_TITLE_MAX_LENGTH)


class CashDeskCreateCommand(CashDeskCreateDTO, Command): ...


class CashDeskUpdateDTO(CashDeskCreateDTO): ...


class CashDeskUpdateCommand(CashDeskUpdateDTO, Command):
    id: ID_T


class CashDeskDeleteCommand(Command):
    id: ID_T


class CashDeskToggleCommand(Command):
    id: ID_T


class CashDeskRebalanceDTO(BasePydanticModel):
    """Set a cash desk balance to an absolute target.

    The client sends the new desired balance (`target_balance`); the backend
    computes the signed delta, records an immutable rebalance-history row, and
    writes a single WalletOperation for the delta. No WalletDocument is created.
    """

    target_balance: Decimal = Field(ge=Decimal("0"))
    operating_expense_id: ID_T
    comment: str
    confirmed_at: ATDatetime
    files_ids: List[ID_T] = Field(default_factory=list)


class CashDeskRebalanceCommand(CashDeskRebalanceDTO, Command):
    cash_desk_id: ID_T
