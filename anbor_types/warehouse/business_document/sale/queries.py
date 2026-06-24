from typing import Optional

from anbor_types import ID_T, ListQuery, Query
from anbor_types.common.enums import StatusEnum


class SaleDocumentListQuery(ListQuery):
    status: Optional[StatusEnum] = None


class SaleDocumentGetQuery(Query):
    id: ID_T


class SaleDocumentGetDetailedQuery(Query):
    id: ID_T
