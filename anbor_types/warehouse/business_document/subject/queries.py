from anbor_types import ID_T, ListQuery, Query


class SubjectListQuery(ListQuery): ...

class SubjectDetailedQuery(Query):
    id: ID_T


class SubjectBalanceQuery(Query):
    id: ID_T
