from decimal import Decimal
from typing import List

import msgspec

from anbor_types.handbook.operating_expense.dto import OperatingExpenseListDTO
from anbor_types.statistics.daily_analytics.dto import DailyAnalyticShortDTO


class WalletIncomeStatementListDTO(msgspec.Struct):
    cost_price: Decimal
    gross_profit: Decimal
    operating_expenses: List[OperatingExpenseListDTO]
    operating_income_total: Decimal
    revenue: Decimal


class WalletCashFlowListDTO(msgspec.Struct):
    cash_desk_balance: Decimal
    analytics: List[DailyAnalyticShortDTO]
