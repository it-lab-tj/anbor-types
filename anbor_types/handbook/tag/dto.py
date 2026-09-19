from datetime import datetime

import msgspec

from anbor_types import ID_T, BasePydanticModel
from anbor_types.common.enums import ContentTypeEnum, StatusEnum


class TagCreateDTO(BasePydanticModel):
    name: str
    color: str
    icon: str


class TagShortListDTO(msgspec.Struct):
    id: ID_T
    name: str


class TagWithDocumentCountListDTO(msgspec.Struct):
    id: ID_T
    name: str
    documents_count: int


class TagUpdateDTO(BasePydanticModel):
    name: str


class TagListDTO(msgspec.Struct):
    id: ID_T
    name: str
    color: str
    icon: str
    content_type: ContentTypeEnum
    status: StatusEnum
    created_at: datetime
