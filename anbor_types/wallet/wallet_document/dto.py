from datetime import datetime
from decimal import Decimal
from typing import List, Optional

import msgspec

from anbor_types import ID_T, BasePydanticModel
from anbor_types.wallet.cash_desk.dto import CashDeskShortListDTO
from anbor_types.handbook.project.dto import ProjectShortListDTO
from anbor_types.identity.user.dto import AuthorInfoShortDTO
from anbor_types.storage.counterparty.dto import CounterpartyShortDTO
from anbor_types.wallet.currency.dto import CurrencyShortDTO
from anbor_types.wallet.constants import WalletDocumentKindEnum


class WalletDocumentListDTO(msgspec.Struct):
    id: ID_T
    cash_desk: CashDeskShortListDTO
    amount: Decimal
    counterparty: str
    confirm_date: datetime
    type: WalletDocumentKindEnum
    currency: CurrencyShortDTO
    created_by: AuthorInfoShortDTO
    vendor_code: Optional[str] = None


class WalletDocumentDetailedDTO(msgspec.Struct):
    id: ID_T
    amount: Decimal
    capstone: str
    cash_desk: CashDeskShortListDTO
    confirm_date: datetime
    counterparty: CounterpartyShortDTO
    created_by: AuthorInfoShortDTO
    type: WalletDocumentKindEnum
    project: ProjectShortListDTO
    files: List[ID_T]
    comment: Optional[str] = None
    converted_capstone: Optional[str] = None
    vendor_code: Optional[str] = None
    converted_amount: Optional[Decimal] = None


class WalletDocumentCreateDTO(BasePydanticModel):
    amount: Decimal
    cash_desk_id: ID_T
    comment: str
    confirm_date: datetime
    counterparty_id: ID_T
    content_id: ID_T
    content_type: str
    currency_id: ID_T
    files_ids: List[ID_T]
    operating_expense_id: ID_T
    project_id: ID_T
    rate: int
    type: WalletDocumentKindEnum
    stock_operation_group_id: Optional[ID_T] = None
