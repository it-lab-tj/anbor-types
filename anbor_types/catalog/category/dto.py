from typing import Optional, List
import msgspec
from anbor_types import ID_T, BasePydanticModel
from anbor_types.common.annotated import ATSingleLineStr
from anbor_types.common.dto import NameIdDTO


class CharValueDTO(BasePydanticModel):
    characteristic_id: ID_T
    value_id: ID_T


class CategoryUpdateDTO(BasePydanticModel):
    name: ATSingleLineStr


class CharValueDetailedDTO(msgspec.Struct):
    characteristic_id: ID_T
    characteristic_name: str
    values: List[NameIdDTO]


class CharacteristicValuePairDTO(msgspec.Struct):
    characteristic_id: ID_T
    characteristic_name: str
    value_id: ID_T
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


class CategoryWithProductCountDTO(msgspec.Struct):
    """One category plus how many catalog entries sit in its subtree.

    ``product_count`` is a rolled-up total: the category's own entries plus
    those of every descendant category, so a parent shows everything beneath it.
    Deliberately carries no ``characteristics``.

    Trimmed to what a category picker needs: ``parent_id`` stays because the
    tree cannot be rebuilt client-side without it, but ``slug``/``created_at``
    are dropped, and so is ``status`` - every row carries whichever status the
    caller asked for, so repeating it per row says nothing.
    """

    id: ID_T
    name: str
    parent_id: Optional[ID_T]
    product_count: int


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
    kind: str
    values: List[CategoryCharacteristicValueDTO]
    is_required: bool


class CategoryCharacteristicsDTO(msgspec.Struct):
    id: ID_T
    name: str
    parent: Optional[ID_T]
    characteristics: List[CategoryCharacteristicDTO]
