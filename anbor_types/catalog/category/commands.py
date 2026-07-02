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

    ``id`` present = existing characteristic (row left untouched, its values
    still synced by name); ``id is None`` = new characteristic to create.
    ``values`` are plain value names, reconciled by name.
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
