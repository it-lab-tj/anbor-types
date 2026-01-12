import msgspec
from pydantic_core import Url

from anbor_types import ID_T


class ImageListDTO(msgspec.Struct):
    id: ID_T
    name: str
    original_url: Url
