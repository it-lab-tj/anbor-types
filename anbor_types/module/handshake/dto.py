from datetime import datetime
from typing import Optional
from uuid import UUID

import msgspec
from pydantic import ConfigDict

from anbor_types import BasePydanticModel
from anbor_types.common.annotated import ATDomainName
from anbor_types.identity.company.dto import CompanyListDTO
from anbor_types.module.annotated import (
    ATBase64UrlPayload,
    ATBase64UrlSignature,
    ATHandshakeNonce,
    ATHandshakeNonceHash,
    ATSigningKeyId,
)
from anbor_types.module.enums import HandshakeKindEnum, HandshakeStatusEnum


class HandshakeInitDTO(BasePydanticModel):
    domain: ATDomainName


# ===== THE SIGNED ENVELOPE =====


class SignedEnvelopeDTO(BasePydanticModel):
    """The request body of every handshake initiation.

    The signature travels in the body rather than in headers, and it covers the
    base64url `payload` string byte for byte, so neither side has to agree on a
    JSON canonicalisation: re-encoding the decoded payload is never necessary
    and never attempted.

    Signature input, UTF-8, `\\n`-separated, in this order::

        key_id \\n timestamp \\n nonce \\n METHOD \\n PATH \\n payload

    `payload` there is the base64url string exactly as sent, not the JSON it
    decodes to. The receiver decodes it only once the signature has verified.
    """

    payload: ATBase64UrlPayload
    key_id: ATSigningKeyId
    timestamp: int
    # 32 random bytes, base64url. Never logged, and on the sending side never
    # stored -- only its sha256 is kept, so a leaked database cannot confirm a
    # handshake.
    #
    # Charset-constrained, not just length-constrained: the signed bytes are
    # newline-joined without length prefixes, so a field able to carry a newline
    # would let an attacker shift a boundary and have two different envelopes
    # produce identical signed bytes.
    nonce: ATHandshakeNonce
    signature: ATBase64UrlSignature

    model_config = ConfigDict(frozen=True)


class HandshakeInitPayloadDTO(msgspec.Struct):
    """What the envelope's `payload` decodes to.

    `anbor_hostname` is this server's own public hostname, and the receiver
    checks it against the hostname its copy of `key_id` is pinned to: a key may
    speak only for the server it belongs to.
    """

    company: CompanyListDTO
    rel_callback_url: str
    anbor_hostname: str


class HandshakeInitAckDTO(msgspec.Struct):
    """The receiver's answer to an initiation: accepted and awaiting a human.

    Carries no secret. Under the Ed25519 handshake the initiator already holds
    everything it needs -- the nonce it generated itself -- so there is nothing
    for the other side to hand back.
    """

    status: HandshakeStatusEnum


# ===== CONFIRMATION (receiver -> initiator) =====


class HandshakeConfirmationDTO(BasePydanticModel):
    """Proof of holding the nonce, nothing else.

    No handshake id: the row is found by `nonce_hash`, and which row may be
    confirmed is decided by the source IP of this request against the address
    the initiation was actually delivered to. A hostname in the body would be
    the caller's own claim about itself, so none is accepted.
    """

    nonce_hash: ATHandshakeNonceHash

    model_config = ConfigDict(frozen=True)


class HandshakeConfirmationResponseDTO(msgspec.Struct):
    api_key: str  # In base64 format. Returned once, never readable again.


# ===== PERSISTENCE =====


class HandshakeCreateDTO(BasePydanticModel):
    id: UUID
    kind: HandshakeKindEnum
    expires_at: int
    status: HandshakeStatusEnum
    domain: str
    # sha256 of the nonce. The nonce itself is never persisted.
    nonce_hash: bytes

    model_config = ConfigDict(frozen=True)


class HandshakeListDTO(msgspec.Struct):
    id: UUID
    kind: HandshakeKindEnum
    status: HandshakeStatusEnum
    expires_at: int
    created_at: datetime
    updated_at: datetime
    # Set once the initiation request has actually been delivered, to the peer
    # address of the socket that carried it. `None` means no confirmation can be
    # accepted for this row at all.
    marketplace_ip: Optional[str] = None
    used_at: Optional[datetime] = None
