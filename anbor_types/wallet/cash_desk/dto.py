from decimal import Decimal

import msgspec

from anbor_types import ID_T


class CashDeskShortListDTO(msgspec.Struct):
    id: ID_T
    title: str


class CashDeskRebalanceResultDTO(msgspec.Struct):
    cash_desk_id: ID_T
    previous_balance: Decimal
    new_balance: Decimal
