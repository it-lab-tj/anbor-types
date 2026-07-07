import msgspec

from anbor_types import ID_T


class AuthorInfoShortDTO(msgspec.Struct):
    id: ID_T
    full_name: str


class StaffMemberShortDTO(msgspec.Struct):
    id: ID_T
    full_name: str
