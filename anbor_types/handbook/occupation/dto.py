import msgspec

from src.app.shared_kernel.types.base_types import ID_T


class OccupationListDTO(msgspec.Struct):
    id: ID_T
    name: str
