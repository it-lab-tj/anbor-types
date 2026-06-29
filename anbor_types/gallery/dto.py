from typing import Optional

import msgspec

from anbor_types import ID_T


class ImageListDTO(msgspec.Struct):
    id: ID_T
    name: str
    original_url: Optional[str]


class ImageOriginalUrlDTO(msgspec.Struct):
    original_url: str


class ImageShortDTO(msgspec.Struct):
    id: ID_T
    original_url: str
