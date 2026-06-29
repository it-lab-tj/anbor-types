from datetime import datetime
from decimal import Decimal
from typing import Optional

import msgspec

from anbor_types import ID_T
from anbor_types.handbook.project.dto import ProjectShortListDTO
from anbor_types.wallet.currency.dto import CurrencyShortDTO
from anbor_types.warehouse.constants.enums import BusinessDocumentActionEnum


class BusinessDocumentSubjectDTO(msgspec.Struct):
    """Subject (debit/credit) short data for the unified document list."""

    id: ID_T
    name: str
    full_name: Optional[str] = None


class BusinessDocumentAuthorDTO(msgspec.Struct):
    """Author short data for the unified document list."""

    id: ID_T
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None


class BusinessDocumentListItemDTO(msgspec.Struct):
    """Kind-agnostic row for the unified business document list.

    A single row shape projected across every document action. Fields that do
    not exist for a given action are ``None`` (e.g. ``credit`` for ADJUSTMENT,
    ``currency``/``rate`` for TRANSFER).
    """

    id: ID_T
    action: BusinessDocumentActionEnum
    vendor_code: str
    amount: Decimal
    created_by: BusinessDocumentAuthorDTO
    debit: Optional[BusinessDocumentSubjectDTO] = None
    credit: Optional[BusinessDocumentSubjectDTO] = None
    currency: Optional[CurrencyShortDTO] = None
    project: Optional[ProjectShortListDTO] = None
    shipped_at: Optional[datetime] = None
    rate: Optional[Decimal] = None
    converted_amount: Optional[Decimal] = None
    items_count: Optional[int] = None
