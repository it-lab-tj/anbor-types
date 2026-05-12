import msgspec

from anbor_types import ID_T


class CounterpartyShortListDTO(msgspec.Struct):
    id: ID_T
    name: str
