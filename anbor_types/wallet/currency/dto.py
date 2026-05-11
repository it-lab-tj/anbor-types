from datetime import datetime

import msgspec

from anbor_types import ID_T
from anbor_types.common.enums import StatusEnum
from anbor_types.identity.user.dto import AuthorShortInfoDTO


class CurrencyListDTO(msgspec.Struct):
    id: ID_T
    name: str
    short_name: str
    code_symbol: str
    code: int
    bid: int
    flag: str
    fractional_unit: str
    created_at: datetime
    updated_at: datetime
    created_by: AuthorShortInfoDTO
    updated_by: AuthorShortInfoDTO
    status: StatusEnum
