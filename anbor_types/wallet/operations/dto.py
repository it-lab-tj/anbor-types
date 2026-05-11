from datetime import datetime
from decimal import Decimal

import msgspec

from anbor_types import ID_T
from anbor_types.handbook.cash_desk.dto import CashDeskShortListDTO
from anbor_types.handbook.cash_desk.operating_expense.dto import (
    OperatingExpenseShortListDTO,
)
from anbor_types.wallet.enums import OperationTypeEnum


class OperationListDTO(msgspec.Struct):
    id: ID_T
    cash_desk: CashDeskShortListDTO
    vendor_code: str
    amount: Decimal
    counterparty: str
    operating_expense: OperatingExpenseShortListDTO
    converted_amount: Decimal
    confirm_date: datetime
    type: OperationTypeEnum
