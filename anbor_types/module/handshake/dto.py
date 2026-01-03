
import datetime
from uuid import UUID

import msgspec
from anbor_types.identity.company.dto import CompanyListDTO
from pydantic import ConfigDict
from anbor_types import BasePydanticModel
from anbor_types.common.annotated import ATDomainName
from anbor_types.module.enums import HandshakeKindEnum, HandshakeStatusEnum


class HandshakeInitDTO(BasePydanticModel):
    domain: ATDomainName


class HandshakeConfirmationDTO(BasePydanticModel):
    handshake_id: UUID
    signature: str  # base64 encoded string


class HandshakeConfirmationResponseDTO(msgspec.Struct):
    api_key: str  # In base64 format


class HandshakeInitRequestDTO(BasePydanticModel):
    rel_callback_url: str
    domain: str
    company: CompanyListDTO


class HandshakeInitResponseDTO(BasePydanticModel):
    handshake_id: UUID
    secret: str  # In base64 format


class HandshakeCreateDTO(BasePydanticModel):
    id: UUID
    kind: HandshakeKindEnum
    expires_at: int
    status: HandshakeStatusEnum
    domain: str
    secret: bytes  # Encrypted bytes on save

    model_config = ConfigDict(frozen=True)


class HandshakeListDTO(msgspec.Struct):
    id: UUID
    kind: HandshakeKindEnum
    status: HandshakeStatusEnum
    expires_at: int
    created_at: datetime
    updated_at: datetime
