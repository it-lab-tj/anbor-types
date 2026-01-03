from typing import Optional

from anbor_types import Command
from anbor_types.catalog.annotated import ATSingleLineStr
from anbor_types.catalog.enums import CategoryKind



class CategoryCreateCommand(Command):
    name: ATSingleLineStr
    parent_id: Optional[int] = None
    image_id: Optional[int] = None
    kind: CategoryKind
