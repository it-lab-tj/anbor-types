from typing import Optional

from anbor_types import ListQuery
from anbor_types.common.enums import StatusEnum


class SaleDocumentListQuery(ListQuery):
    status: Optional[StatusEnum] = None
