from anbor_types import ID_T, ListQuery, Query
from anbor_types.warehouse.constants.enums import SubjectKindEnum


class SubjectListQuery(ListQuery):
    kind: SubjectKindEnum
    status: int


class SubjectDetailedQuery(Query):
    id: ID_T
