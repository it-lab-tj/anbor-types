import msgspec

from anbor_types import ID_T


class OperatingExpenseShortListDTO(msgspec.Struct):
    id: ID_T
    title: str
