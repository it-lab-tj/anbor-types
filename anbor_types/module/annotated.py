from typing import Annotated

from pydantic import StringConstraints

from anbor_types.module.constraints import (
    BASE64URL_REGEX,
    CATALOG_FEED_CURSOR_MAX_LENGTH,
    CATALOG_FEED_CURSOR_REGEX,
    HANDSHAKE_NONCE_B64_LENGTH,
    HANDSHAKE_NONCE_HASH_B64_LENGTH,
    SIGNING_KEY_ID_MAX_LENGTH,
    SIGNING_KEY_ID_REGEX,
)

# The feed cursor is opaque to the consumer but not unvalidated: the shape is
# declared here so a malformed one is a 400 rather than a failed `xid8` cast.
type ATCatalogFeedCursor = Annotated[
    str,
    StringConstraints(
        max_length=CATALOG_FEED_CURSOR_MAX_LENGTH,
        pattern=CATALOG_FEED_CURSOR_REGEX,
        strip_whitespace=True,
    ),
]

type ATSigningKeyId = Annotated[
    str,
    StringConstraints(
        max_length=SIGNING_KEY_ID_MAX_LENGTH,
        pattern=SIGNING_KEY_ID_REGEX,
        strip_whitespace=True,
    ),
]

type ATHandshakeNonce = Annotated[
    str,
    StringConstraints(
        min_length=HANDSHAKE_NONCE_B64_LENGTH,
        max_length=HANDSHAKE_NONCE_B64_LENGTH,
        pattern=BASE64URL_REGEX,
    ),
]

type ATHandshakeNonceHash = Annotated[
    str,
    StringConstraints(
        min_length=HANDSHAKE_NONCE_HASH_B64_LENGTH,
        max_length=HANDSHAKE_NONCE_HASH_B64_LENGTH,
        pattern=BASE64URL_REGEX,
    ),
]

# base64url of the UTF-8 JSON bytes of a handshake payload, and of an Ed25519
# signature. Both are bounded so an oversized body is refused before any
# decoding or signature work happens.
type ATBase64UrlPayload = Annotated[
    str, StringConstraints(max_length=65536, pattern=BASE64URL_REGEX)
]
type ATBase64UrlSignature = Annotated[
    str, StringConstraints(min_length=86, max_length=86, pattern=BASE64URL_REGEX)
]
