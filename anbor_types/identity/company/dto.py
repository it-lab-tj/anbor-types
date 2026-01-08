import msgspec
from anbor_types import ID_T


class CompanyListDTO(msgspec.Struct):
    id: ID_T
    name: str
    nick: str
    phone_number: str
    email: str
