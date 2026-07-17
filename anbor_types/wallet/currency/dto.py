from datetime import datetime

import msgspec

from anbor_types import ID_T
from anbor_types.identity.user.dto import AuthorInfoShortDTO


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
    created_by: AuthorInfoShortDTO
    updated_by: AuthorInfoShortDTO


class CurrencyShortListDTO(msgspec.Struct):
    id: ID_T
    name: str
    code_symbol: str


class CurrencyShortDTO(msgspec.Struct):
    id: ID_T
    code_symbol: str


class CurrencyCodeSymbolDTO(msgspec.Struct):
    code_symbol: str


class CurrencyDetailedInternalDTO(msgspec.Struct):
    id: ID_T
    code_symbol: str
    bid: int
