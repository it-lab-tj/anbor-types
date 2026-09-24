from datetime import datetime
from typing import Annotated

import msgspec
from pydantic import Field

from anbor_types import ID_T, BasePydanticModel
from anbor_types.common.enums import ContentTypeEnum, StatusEnum
from anbor_types.handbook import constraints


class TagCreateDTO(BasePydanticModel):
    name: str
    text_color: Annotated[
        int,
        Field(
            required=True,
            ge=constraints.TAG_TEXT_COLOR_MIN_VALUE,
            le=constraints.TAG_TEXT_COLOR_MAX_VALUE,
        ),
    ]
    icon: Annotated[
        int,
        Field(
            required=True,
            ge=constraints.TAG_ICON_MIN_VALUE,
            le=constraints.TAG_ICON_MIN_VALUE,
        ),
    ]
    background_color: Annotated[
        int,
        Field(
            required=True,
            ge=constraints.TAG_BG_COLOR_MIN_VALUE,
            le=constraints.TAG_BG_COLOR_MAX_VALUE,
        ),
    ]


class TagShortListDTO(msgspec.Struct):
    id: ID_T
    name: str


class TagWithDocumentsCountListDTO(msgspec.Struct):
    id: ID_T
    name: str
    documents_count: int


class TagUpdateDTO(BasePydanticModel):
    name: str
    text_color: Annotated[
        int,
        Field(
            ge=constraints.TAG_TEXT_COLOR_MIN_VALUE,
            le=constraints.TAG_TEXT_COLOR_MAX_VALUE,
        ),
    ]
    icon: Annotated[
        int,
        Field(
            ge=constraints.TAG_ICON_MIN_VALUE,
            le=constraints.TAG_ICON_MAX_VALUE,
        ),
    ]
    background_color: Annotated[
        int,
        Field(
            ge=constraints.TAG_BG_COLOR_MIN_VALUE,
            le=constraints.TAG_BG_COLOR_MAX_VALUE,
        ),
    ]


class TagListDTO(msgspec.Struct):
    id: ID_T
    name: str
    content_type: ContentTypeEnum
    status: StatusEnum
    created_at: datetime
    text_color: int
    background_color: int
    icon: int
