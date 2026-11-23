import msgspec

from src.app.shared_kernel.types.base_types import ID_T


class CityListDTO(msgspec.Struct):
    id: ID_T
    name: str
