from typing import Optional

from anbor_types import ID_T, ListQuery, Query
from anbor_types.common.enums import StatusEnum


class ServiceDocumentListQuery(ListQuery):
    status: Optional[StatusEnum] = None


class ServiceDocumentGetQuery(Query):
    id: ID_T


class ServiceDocumentGetDetailedQuery(Query):
    id: ID_T
