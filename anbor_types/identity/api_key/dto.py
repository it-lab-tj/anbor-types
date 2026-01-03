import msgspec

from anbor_types import ID_T, BasePydanticModel


class ApiKeyCreateDTO(BasePydanticModel):
    key: bytes


class ApiKeyListDTO(msgspec.Struct):
    id: ID_T
    # Api key, not a signature. In base64 format. If type is str, then its base64, raw api key otherwise
    key: bytes | str
