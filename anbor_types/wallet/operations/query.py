from datetime import datetime
from decimal import Decimal
from typing import List

from anbor_types import ID_T, ListQuery
from anbor_types.wallet.constants import OperationTypeEnum


class OperationListQuery(ListQuery):
    amount_max: Decimal
    amount_min: Decimal
    cash_desk_id: ID_T
    converted_amount_max: Decimal
    converted_amount_min: Decimal
    counterparty_id: ID_T
    created_at_after: datetime
    created_at_before: datetime
    created_by_id: ID_T
    updated_by_id: ID_T
    currency_id: ID_T
    operating_expense_id: ID_T
    ordering: str
    paid: str
    project_id: ID_T
    search: str
    type: OperationTypeEnum
    vendor_codes: List[str]
