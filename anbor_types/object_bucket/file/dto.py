import msgspec

from anbor_types import ID_T, BasePydanticModel


class FileCreateDTO(BasePydanticModel):
    name: str
    abs_path: str


class FileListDTO(msgspec.Struct):
    id: ID_T
    name: str
    file: str


class FileDetailedDTO(FileListDTO):
    extension: str
