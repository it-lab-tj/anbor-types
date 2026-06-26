from anbor_types import ListQuery, Query, ID_T
from src.app.shared_kernel.utils.filters.mixins import QueryFilterMixin


class ServiceListQuery(ListQuery, QueryFilterMixin): ...


class ServiceDetailedQuery(Query):
    id: ID_T
