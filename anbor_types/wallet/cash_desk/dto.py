from datetime import datetime
from decimal import Decimal
from typing import Optional

import msgspec

from anbor_types import ID_T
from anbor_types.common.enums import StatusEnum
from anbor_types.identity.user.dto import AuthorInfoShortDTO
from anbor_types.wallet.operating_expense.dto import OperatingExpenseShortListDTO


class CashDeskShortListDTO(msgspec.Struct):
    id: ID_T
    title: str


class CashDeskListDTO(msgspec.Struct):
    id: ID_T
    title: str
    balance: Decimal
    status: StatusEnum
    created_at: datetime
    updated_at: datetime
    created_by: Optional[AuthorInfoShortDTO] = None


class CashDeskDetailedDTO(msgspec.Struct):
    id: ID_T
    title: str
    balance: Decimal
    status: StatusEnum
    created_at: datetime
    updated_at: datetime
    created_by: Optional[AuthorInfoShortDTO] = None
    updated_by: Optional[AuthorInfoShortDTO] = None


class CashDeskRebalanceResultDTO(msgspec.Struct):
    cash_desk_id: ID_T
    previous_balance: Decimal
    new_balance: Decimal


class CashDeskRebalanceHistoryListDTO(msgspec.Struct):
    """Row of the immutable rebalance history. Field names follow the model;
    `diff` is `new_balance - previous_balance` (None on the very first
    rebalance, where no previous balance was recorded)."""

    id: ID_T
    new_balance: Decimal
    created_at: datetime
    operating_expense: OperatingExpenseShortListDTO
    previous_balance: Optional[Decimal] = None
    diff: Optional[Decimal] = None
    created_by: Optional[AuthorInfoShortDTO] = None
