from anbor_types import ID_T, ListQuery
from anbor_types.api.queries import ShortListQuery


class CashDeskRebalanceHistoryListQuery(ListQuery):
    # Comes from the URL path, not from query params.
    cash_desk_id: ID_T


class CashDeskShortListQuery(ShortListQuery): ...
