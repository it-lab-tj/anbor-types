from typing import Optional, List
import msgspec
from anbor_types import ID_T, BasePydanticModel


class CharValueDTO(BasePydanticModel):
    characteristic_id: ID_T
    value_id: ID_T


class CharValuesListDTO(msgspec.Struct):
    characteristic_id: ID_T
    value_id: ID_T


class ValueListDTO(msgspec.Struct):
    id: ID_T
    name: str
    characteristic_id: ID_T


class CharacteristicListDTO(msgspec.Struct):
    id: ID_T
    name: str
    values: List[ValueListDTO]


class CategoryDetailedDTO(msgspec.Struct):
    id: ID_T
    name: str
    parent_id: Optional[ID_T]
    characteristics: List[CharacteristicListDTO]
