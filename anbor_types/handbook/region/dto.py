import msgspec

from anbor_types import ID_T


class RegionShortDTO(msgspec.Struct):
    id: ID_T
    name: str
