from datetime import datetime
from decimal import Decimal
from typing import List, Optional

import msgspec

from anbor_types import ID_T
from anbor_types.handbook.cash_desk.dto import CashDeskShortListDTO
from anbor_types.handbook.project.dto import ProjectShortListDTO
from anbor_types.identity.user.dto import AuthorShortInfoDTO
from anbor_types.storage.counterparty.dto import CounterpartyShortListDTO
from anbor_types.wallet.currency.dto import CurrencyShortListDTO
from anbor_types.wallet.enums import OperationTypeEnum


class OperationListDTO(msgspec.Struct):
    id: ID_T
    cash_desk: CashDeskShortListDTO
    vendor_code: Optional[str] = None
    amount: Decimal
    counterparty: str
    converted_amount: Decimal
    confirm_date: datetime
    type: OperationTypeEnum
    currency: CurrencyShortListDTO
    created_by: AuthorShortInfoDTO


class OperationCreateListDTO(OperationListDTO): ...


class OperationDetailedListDTO(msgspec.Struct):
    id: ID_T
    amount: Decimal
    vendor_code: Optional[str] = None
    capstone: str
    cash_desk: CashDeskShortListDTO
    comment: Optional[str] = None
    confirm_date: datetime
    converted_amount: Optional[Decimal] = None
    converted_capstone: Optional[str] = None
    counterparty: CounterpartyShortListDTO
    created_by: AuthorShortInfoDTO
    type: OperationTypeEnum
    files: List[ID_T]
    project: ProjectShortListDTO
