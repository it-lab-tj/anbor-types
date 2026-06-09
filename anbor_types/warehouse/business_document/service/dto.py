from datetime import datetime
from decimal import Decimal
from typing import Optional

import msgspec

from anbor_types import ID_T
from anbor_types.warehouse.business_document.subject.dto import (
    SubjectForBusinessDocumentShortDataDTO,
)


class ServiceShortDTO(msgspec.Struct):
    id: ID_T
    name: str
    selling_price: Decimal


class ServiceOperationListDTO(msgspec.Struct):
    id: ID_T
    performer: SubjectForBusinessDocumentShortDataDTO
    counterparty: SubjectForBusinessDocumentShortDataDTO
    service: ServiceShortDTO
    count: Decimal
    amount: Decimal
    created_at: datetime
    completed_at: Optional[datetime] = None


class ServiceOperationDetailedDTO(msgspec.Struct):
    id: ID_T
    performer: SubjectForBusinessDocumentShortDataDTO
    counterparty: SubjectForBusinessDocumentShortDataDTO
    service: ServiceShortDTO
    count: Decimal
    amount: Decimal
    created_at: datetime
    company_id: ID_T
    completed_at: Optional[datetime] = None
