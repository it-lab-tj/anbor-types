import msgspec
from anbor_types import ID_T


class HandshakeRequestResult(msgspec.Struct):
    """Result after first handshake request"""

    handshake_id: ID_T
    secret: str # In base 64 format