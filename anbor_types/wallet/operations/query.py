from datetime import datetime
from decimal import Decimal
from typing import List, Optional

from anbor_types import ID_T, ListQuery
from anbor_types.wallet.constants import OperationTypeEnum


class OperationListQuery(ListQuery):
    amount_max: Optional[Decimal] = None
    amount_min: Optional[Decimal] = None
    cash_desk_id: Optional[ID_T] = None
    converted_amount_max: Optional[Decimal] = None
    converted_amount_min: Optional[Decimal] = None
    counterparty_id: Optional[ID_T] = None
    created_at_after: Optional[datetime] = None
    created_at_before: Optional[datetime] = None
    created_by_id: Optional[ID_T] = None
    updated_by_id: Optional[ID_T] = None
    currency_id: Optional[ID_T] = None
    operating_expense_id: Optional[ID_T] = None
    ordering: Optional[str] = None
    paid: Optional[str] = None
    project_id: Optional[ID_T] = None
    search: Optional[str] = None
    type: Optional[OperationTypeEnum] = None
    vendor_codes: Optional[List[str]] = None
