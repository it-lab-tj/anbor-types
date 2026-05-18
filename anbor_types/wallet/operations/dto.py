from datetime import datetime
from decimal import Decimal
from typing import List, Optional

import msgspec

from anbor_types import ID_T
from anbor_types.wallet.cash_desk.dto import CashDeskShortListDTO
from anbor_types.handbook.project.dto import ProjectShortListDTO
from anbor_types.identity.user.dto import AuthorInfoShortDTO
from anbor_types.storage.counterparty.dto import CounterpartyShortDTO
from anbor_types.wallet.currency.dto import CurrencyShortDTO
from anbor_types.wallet.constants import OperationKindEnum


class OperationListDTO(msgspec.Struct):
    id: ID_T
    cash_desk: CashDeskShortListDTO
    amount: Decimal
    counterparty: str
    confirm_date: datetime
    type: OperationKindEnum
    currency: CurrencyShortDTO
    created_by: AuthorInfoShortDTO
    vendor_code: Optional[str] = None


class OperationDetailedDTO(msgspec.Struct):
    id: ID_T
    amount: Decimal
    capstone: str
    cash_desk: CashDeskShortListDTO
    confirm_date: datetime
    counterparty: CounterpartyShortDTO
    created_by: AuthorInfoShortDTO
    type: OperationKindEnum
    project: ProjectShortListDTO
    files: List[ID_T]
    comment: Optional[str] = None
    converted_capstone: Optional[str] = None
    vendor_code: Optional[str] = None
    converted_amount: Optional[Decimal] = None
