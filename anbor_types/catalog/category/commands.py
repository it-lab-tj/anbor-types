from typing import List, Optional

from anbor_types import BasePydanticModel, Command, ID_T
from anbor_types.catalog.annotated import ATSingleLineStr
from anbor_types.catalog.enums import CategoryKindEnum


class CategoryCreateCommand(Command):
    name: ATSingleLineStr
    parent_id: Optional[int] = None
    image_id: Optional[int] = None
    kind: CategoryKindEnum


class CategoryUpdateCommand(Command):
    id: ID_T
    name: ATSingleLineStr


class CharacteristicSetItem(BasePydanticModel):
    """One characteristic in a category's full-state characteristics payload.

    ``id`` present = existing characteristic: ``name``, ``kind`` and
    ``is_required`` are written onto the row, its values synced by name.
    ``id is None`` = new characteristic to create. Existing characteristics of
    the category that no payload item names are deleted.

    ``values`` are plain value names (not the ``{id, name}`` objects the GET
    returns), reconciled by name. ``slug`` is derived once at creation and does
    not follow a later rename.
    """

    name: str
    kind: str
    values: List[str]
    is_required: bool
    id: Optional[ID_T] = None


class CategorySetCharacteristicsCommand(Command):
    category_id: ID_T
    characteristics: List[CharacteristicSetItem]


class CategoryDuplicateCommand(Command):
    id: ID_T


class CategoryDeleteCommand(Command):
    id: ID_T


class CategoryToggleCommand(BasePydanticModel, Command):
    id: ID_T


class CharacteristicDeleteCommand(Command):
    id: ID_T


class CharAddValueCommand(Command):
    value: str


class CharacateristicAddValueCommand(Command):
    characteristic_id: ID_T
    value: str
