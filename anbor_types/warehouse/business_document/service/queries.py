from anbor_types import ID_T, ListQuery, Query


class ServiceOperationListQuery(ListQuery):
    pass


class ServiceOperationDetailedQuery(Query):
    id: ID_T
