from anbor_types import ID_T, ListQuery, Query
from src.app.shared_kernel.utils.filters.mixins import QueryFilterMixin


class ServiceDocumentListQuery(ListQuery, QueryFilterMixin): ...


class ServiceDocumentGetQuery(Query):
    id: ID_T


class ServiceDocumentGetDetailedQuery(Query):
    id: ID_T
