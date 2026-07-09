from anbor_types import ID_T, ListQuery, Query
from anbor_types.api.queries import ShortListQuery
from anbor_types.api.types import OrderingAllowedFieldsT
from anbor_types.utils.mixins import OrderingQueryMixin


class CashDeskRebalanceHistoryListQuery(ListQuery):
    # Comes from the URL path, not from query params.
    cash_desk_id: ID_T


class CashDeskShortListQuery(ShortListQuery): ...


class CashDeskListQuery(ShortListQuery, OrderingQueryMixin):
    _ordering_allowed_fields: OrderingAllowedFieldsT = {
        "title",
        "balance",
        "created_at",
    }


class CashDeskDetailedQuery(Query):
    id: ID_T
