from anbor_types import ID_T, ListQuery, Query


class ServiceDocumentListQuery(ListQuery): ...


class ServiceDocumentGetQuery(Query):
    id: ID_T


class ServiceDocumentGetDetailedQuery(Query):
    id: ID_T
