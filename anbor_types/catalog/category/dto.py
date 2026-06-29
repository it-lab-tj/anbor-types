from typing import Optional, List
import msgspec
from anbor_types import ID_T, BasePydanticModel


class CharValueDTO(BasePydanticModel):
    characteristic_id: ID_T
    value_id: ID_T


class CharValuesListDTO(msgspec.Struct):
    characteristic_id: ID_T
    value_id: ID_T


class CharValueDetailedDTO(CharValuesListDTO):
    characteristic_name: str
    value_name: str


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


class CategoryShortDTO(msgspec.Struct):
    id: ID_T
    name: str
    slug: str


class CategoryCharacteristicValueDTO(msgspec.Struct):
    id: ID_T
    name: str


class CategoryCharacteristicDTO(msgspec.Struct):
    id: ID_T
    name: str
    type: str
    values: List[CategoryCharacteristicValueDTO]
    is_required: bool


class CategoryCharacteristicsDTO(msgspec.Struct):
    id: ID_T
    name: str
    parent: Optional[ID_T]
    characteristics: List[CategoryCharacteristicDTO]
