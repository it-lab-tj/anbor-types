import msgspec

from anbor_types import ID_T


class AuthorShortInfoDTO(msgspec.Struct):
    id: ID_T
    full_name: str
