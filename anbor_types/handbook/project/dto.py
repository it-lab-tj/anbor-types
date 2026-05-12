import msgspec

from anbor_types import ID_T


class ProjectShortListDTO(msgspec.Struct):
    id: ID_T
    name: str
