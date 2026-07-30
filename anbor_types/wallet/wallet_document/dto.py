from datetime import datetime
from decimal import Decimal
from typing import Annotated, List, Optional, Self

import msgspec
from pydantic import Field, model_validator
from pydantic_core import PydanticCustomError

from anbor_types import ID_T, BasePydanticModel
from anbor_types.common.annotated import ATComment, ATDatetime, ATFileIds
from anbor_types.common.dto import FileShortDTO
from anbor_types.common.enums import ContentTypeEnum
from anbor_types.wallet.cash_desk.dto import CashDeskShortListDTO
from anbor_types.handbook.project.dto import ProjectShortListDTO
from anbor_types.identity.user.dto import AuthorInfoShortDTO
from anbor_types.storage.counterparty.dto import CounterpartyShortDTO
from anbor_types.wallet.currency.dto import CurrencyShortDTO, CurrencyShortListDTO
from anbor_types.warehouse.business_document.subject.dto import SubjectShortDTO
from anbor_types.wallet.constants import WalletDocumentKindEnum
from anbor_types.wallet.operating_expense.dto import OperatingExpenseShortListDTO


class WalletDocumentListDTO(msgspec.Struct):
    id: ID_T
    cash_desk: CashDeskShortListDTO
    amount: Decimal
    confirmed_at: datetime
    kind: WalletDocumentKindEnum
    created_by: AuthorInfoShortDTO
    subject: Optional[SubjectShortDTO] = None
    currency: Optional[CurrencyShortDTO] = None
    vendor_code: Optional[str] = None


class WalletDocumentDetailedDTO(msgspec.Struct):
    """Detailed wallet document (income/expense payment).

    `vendor_code` / `storage` come from the referenced business document and
    are None when the document has no business-document reference. `receiver`
    is the payment counterparty (transfers, whose content is a cash desk, get
    None for now).
    """

    id: ID_T
    amount: Decimal
    cash_desk: CashDeskShortListDTO
    kind: WalletDocumentKindEnum
    created_at: datetime
    confirmed_at: datetime
    created_by: AuthorInfoShortDTO
    operating_expense: OperatingExpenseShortListDTO
    vendor_code: Optional[str] = None
    receiver: Optional[CounterpartyShortDTO] = None
    storage: Optional[SubjectShortDTO] = None
    currency: Optional[CurrencyShortListDTO] = None
    project: Optional[ProjectShortListDTO] = None
    comment: Optional[str] = None
    files: Optional[List[FileShortDTO]] = None


class WalletDocumentCreateDTO(BasePydanticModel):
    amount: Annotated[Decimal, Field(gt=Decimal("0"), le=Decimal("9999999999.9999"))]
    cash_desk_id: ID_T
    comment: ATComment
    confirmed_at: ATDatetime
    content_id: Optional[ID_T] = None
    content_type: Optional[ContentTypeEnum] = None
    currency_id: ID_T
    files_ids: List[ID_T]
    operating_expense_id: ID_T
    project_id: ID_T
    rate: Decimal
    kind: WalletDocumentKindEnum
    business_document_id: Optional[ID_T] = None

    @model_validator(mode="after")
    @classmethod
    def validate(cls, v: Self) -> Self:
        if v.content_type is None and v.content_id is not None:
            field = "content_type"

        elif v.content_id is None and v.content_type is not None:
            field = "content_id"

        else:
            return v

        raise PydanticCustomError(
            "missing_paired_field",
            "{field} is required when its pair is set",
            {"field": field},
        )


class WalletDocumentUpdateDTO(BasePydanticModel):
    amount: Annotated[Decimal, Field(gt=Decimal("0"), le=Decimal("9999999999.9999"))]
    files_ids: List[ID_T]
    comment: ATComment
    project_id: ID_T
    operating_expense_id: ID_T


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
    file_ids: Optional[ATFileIds] = Field(default=None)


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
