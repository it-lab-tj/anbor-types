from anbor_types import ID_T, ListQuery


class CashDeskRebalanceHistoryListQuery(ListQuery):
    # Comes from the URL path, not from query params.
    cash_desk_id: ID_T
