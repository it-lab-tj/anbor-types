import msgspec

from anbor_types import ID_T


class AuthorShortInfoDTO(msgspec.Struct):
    id: ID_T
    username: str
    email: str
    full_name: str
