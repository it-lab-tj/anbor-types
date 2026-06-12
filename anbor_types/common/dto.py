import msgspec

from anbor_types import ID_T


class FileShortDTO(msgspec.Struct):
    id: ID_T
    name: str
    file: str


class NameDTO(msgspec.Struct):
    """Universal dto for storing only `name`"""

    name: str
