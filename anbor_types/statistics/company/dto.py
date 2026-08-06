from decimal import Decimal

import msgspec


class CompanyAnalyticsSummaryDTO(msgspec.Struct):
    """Company-wide money totals for the analytics summary panel.

    Balance sign convention across every subject kind: a subject that **owes the
    company** carries a NEGATIVE balance, one the **company owes** carries a
    POSITIVE one. `clients_debt` and `company_debt_total` are the two sides of
    that split, which is why the first is returned as an absolute value.
    """

    # Total cost price of the products held across all storages.
    storage_cost_price: Decimal
    # Total the clients owe the company, as a positive amount.
    clients_debt: Decimal
    # Total balance held across all cash desks.
    cash_desks_total: Decimal
    # Total the company owes its clients.
    company_debt_total: Decimal
    # Total balance across all performers: positive means the company owes them,
    # negative means they owe the company.
    performers_total: Decimal
