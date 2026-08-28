from datetime import datetime

import msgspec

from anbor_types import ID_T, BasePydanticModel
from anbor_types.common.enums import ContentTypeEnum, StatusEnum


class TagCreateDTO(BasePydanticModel):
    name: str


class TagShortListDTO(msgspec.Struct):
    id: ID_T
    name: str


class TagUpdateDTO(BasePydanticModel):
    name: str


class TagListDto(msgspec.Struct):
    id: ID_T
    name: str
    content_type: ContentTypeEnum
    status: StatusEnum
    created_at: datetime
