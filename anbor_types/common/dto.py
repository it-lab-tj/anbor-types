import msgspec

from anbor_types import ID_T


class FileShortDTO(msgspec.Struct):
    id: ID_T
    name: str
    file: str
