import msgspec

from anbor_types import ID_T


class CashDeskShortListDTO(msgspec.Struct):
    id: ID_T
    title: str
