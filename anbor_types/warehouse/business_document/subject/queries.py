from anbor_types import ListQuery
from anbor_types.warehouse.constants.enums import SubjectKindEnum


class SubjectListQuery(ListQuery):
    kind: SubjectKindEnum
    status: int
