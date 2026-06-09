from anbor_types import ListQuery, Query, ID_T


class ServiceListQuery(ListQuery): ...


class ServiceDetailedQuery(Query):
    id: ID_T
