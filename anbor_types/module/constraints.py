# Feed cursor: `<xid8>:<uuid>`, e.g. `6748:0190f2c1-8a3e-7c44-b2d1-9f4e8a1c2b30`.
# `xid8` is an unsigned 64-bit transaction id, so up to 20 digits.
CATALOG_FEED_CURSOR_REGEX = (
    r"^\d{1,20}:"
    r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$"
)
CATALOG_FEED_CURSOR_MAX_LENGTH = 57

# The cursor a consumer starts from. Transaction id 1 is `FrozenTransactionId`,
# below every real one, and the nil UUID sorts before every row id, so this
# admits the whole catalog.
CATALOG_FEED_INITIAL_CURSOR = "0:00000000-0000-0000-0000-000000000000"

CATALOG_FEED_DEFAULT_LIMIT = 100
CATALOG_FEED_MAX_LIMIT = 500

# A signing key id, e.g. `anbor-2026-11`.
SIGNING_KEY_ID_MAX_LENGTH = 64
SIGNING_KEY_ID_REGEX = r"^[a-z0-9][a-z0-9._-]{0,62}[a-z0-9]$"

# base64url of 32 random bytes, unpadded.
HANDSHAKE_NONCE_B64_LENGTH = 43
# base64url of a sha256 digest, unpadded.
HANDSHAKE_NONCE_HASH_B64_LENGTH = 43
BASE64URL_REGEX = r"^[A-Za-z0-9_-]+$"

# How far a handshake envelope's timestamp may sit from the receiver's clock.
HANDSHAKE_TIMESTAMP_SKEW_SECONDS = 20
