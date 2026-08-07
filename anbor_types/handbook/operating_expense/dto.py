from decimal import Decimal

import msgspec

from anbor_types import ID_T


class OperatingExpenseListDTO(msgspec.Struct):
    id: ID_T
    title: str
    amount: Decimal
