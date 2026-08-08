from datetime import datetime
from decimal import Decimal
from typing import Optional

import msgspec

from anbor_types import ID_T
from anbor_types.common.dto import NameIdDTO
from anbor_types.identity.user.dto import AuthorInfoShortDTO
from anbor_types.wallet.currency.dto import CurrencyCodeSymbolDTO
from anbor_types.warehouse.business_document.subject.dto import SubjectShortDTO
from anbor_types.warehouse.constants.enums import BusinessDocumentActionEnum


class CatalogEntryHistoryListDTO(msgspec.Struct):
    """One line of a catalog entry's movement history.

    `subject` is the document's other party from the entry's point of view:
    debit on sale, credit on purchase, counterparty on service, storage on
    adjustment, debit on transfer. `amount` is the line total after its own
    discount.
    """

    id: ID_T
    business_document_id: ID_T
    action: BusinessDocumentActionEnum
    vendor_code: str
    count: Decimal
    price: Decimal
    amount: Decimal
    created_by: AuthorInfoShortDTO
    shipped_at: Optional[datetime] = None
    currency: Optional[CurrencyCodeSymbolDTO] = None
    project: Optional[NameIdDTO] = None
    subject: Optional[SubjectShortDTO] = None
