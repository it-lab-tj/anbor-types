from datetime import datetime
from decimal import Decimal
from typing import List, Optional

import msgspec

from anbor_types import ID_T, BasePydanticModel
from anbor_types.common.dto import FileShortDTO
from anbor_types.common.enums import ContentTypeEnum
from anbor_types.wallet.cash_desk.dto import CashDeskShortListDTO
from anbor_types.handbook.project.dto import ProjectShortListDTO
from anbor_types.identity.user.dto import AuthorInfoShortDTO
from anbor_types.storage.counterparty.dto import CounterpartyShortDTO
from anbor_types.wallet.currency.dto import CurrencyShortDTO
from anbor_types.wallet.constants import WalletDocumentKindEnum
from anbor_types.wallet.operating_expense.dto import OperatingExpenseShortListDTO


class WalletDocumentListDTO(msgspec.Struct):
    id: ID_T
    cash_desk: CashDeskShortListDTO
    amount: Decimal
    confirmed_at: datetime
    kind: WalletDocumentKindEnum
    created_by: AuthorInfoShortDTO
    # Transfers carry no currency. For a transfer, `cash_desk` is the source
    # desk; the destination desk is the document's content (content_type=
    # CASH_DESK, content_id=<desk id>).
    currency: Optional[CurrencyShortDTO] = None
    vendor_code: Optional[str] = None


class WalletDocumentDetailedDTO(msgspec.Struct):
    id: ID_T
    amount: Decimal
    capstone: str
    cash_desk: CashDeskShortListDTO
    confirmed_at: datetime
    created_by: AuthorInfoShortDTO
    type: WalletDocumentKindEnum
    project: ProjectShortListDTO
    files: List[ID_T]
    # Optional because transfers have no counterparty.
    counterparty: Optional[CounterpartyShortDTO] = None
    comment: Optional[str] = None
    converted_capstone: Optional[str] = None
    vendor_code: Optional[str] = None
    converted_amount: Optional[Decimal] = None


class WalletDocumentCreateDTO(BasePydanticModel):
    amount: Decimal
    cash_desk_id: ID_T
    comment: str
    confirmed_at: datetime
    content_id: ID_T
    content_type: ContentTypeEnum
    currency_id: ID_T
    files_ids: List[ID_T]
    operating_expense_id: ID_T
    project_id: ID_T
    rate: Decimal
    kind: WalletDocumentKindEnum
    business_document_id: Optional[ID_T] = None


class WalletDocumentUpdateDTO(BasePydanticModel):
    amount: Decimal
    confirmed_at: datetime
    files_ids: List[ID_T]
    comment: str
    project_id: ID_T
    cash_desk_id: ID_T


class WalletDocumentTransferCreateDTO(BasePydanticModel):
    """Single-currency transfer between two cash desks (API input only).

    Double-entry: `debit_id` is the destination desk (receives money,
    increased), `credit_id` is the source desk (money leaves, decreased). The
    same `amount` moves on both sides; no currency conversion. The handler
    turns this into one wallet document (type=TRANSFER) + two wallet operations.
    """

    debit_id: ID_T
    credit_id: ID_T
    amount: Decimal
    operating_expense_id: ID_T
    comment: str
    file_ids: List[ID_T]


class WalletTransferListDTO(msgspec.Struct):
    """Transfer as shown in lists / returned on create.

    `debit` is the destination desk (increased), `credit` the source desk
    (decreased) — the new names for the legacy cash_desk_to / cash_desk_from.
    """

    id: ID_T
    debit: CashDeskShortListDTO
    credit: CashDeskShortListDTO
    amount: Decimal
    created_at: datetime
    created_by: AuthorInfoShortDTO
    operating_expense: OperatingExpenseShortListDTO
    files: List[FileShortDTO]
    comment: Optional[str] = None
