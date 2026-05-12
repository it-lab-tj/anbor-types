from anbor_types import ListQuery
from anbor_types.common.enums import StatusEnum


class CurrencyListQuery(ListQuery):
    status: StatusEnum
