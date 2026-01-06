from typing import Optional
import msgspec
from anbor_types import ID_T, BasePydanticModel


class CharValueDTO(BasePydanticModel):
    characteristic_id: ID_T
    value_id: ID_T


class ValuesListDTO(msgspec.Struct):
    id: ID_T
    name: str


class CharacteristicDetailedDTO(msgspec.Struct):
    id: ID_T
    name: str
    values: ValuesListDTO


class CategoryDetailedDTO(msgspec.Struct):
    id: ID_T
    name: str
    parent_id: Optional[ID_T]
    characteristic: CharacteristicDetailedDTO
