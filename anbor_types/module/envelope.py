"""The wire format of a signed handshake envelope, shared by both sides.

Signer and verifier have to agree on the signed bytes exactly, so the
construction lives here rather than being written twice. A divergence between
two copies of this would look like an attack at the far end -- a valid request
rejected as a bad signature -- and would be very hard to read from the logs.
"""

import base64

# Fields are joined with a newline and never length-prefixed, which is safe
# only because none of them can contain one: `key_id` and the base64url fields
# are regex-constrained, `timestamp` is an int, and METHOD/PATH come from the
# request line. Keep it that way, or an attacker could shift a boundary and
# have two different requests produce the same signed bytes.
_SEPARATOR = "\n"


def signature_input(
    *,
    key_id: str,
    timestamp: int,
    nonce: str,
    method: str,
    path: str,
    payload: str,
) -> bytes:
    """The exact bytes an envelope's signature covers.

    `payload` is the base64url string as it travels, not the JSON it decodes
    to: signing the encoded form is what removes any need to agree on a JSON
    canonicalisation, and it lets the verifier check the signature *before*
    decoding anything.
    """
    return _SEPARATOR.join(
        (key_id, str(timestamp), nonce, method.upper(), path, payload)
    ).encode("utf-8")


def b64url_encode(raw: bytes) -> str:
    """Unpadded base64url. Padding carries no information and `=` would have to
    be excluded from, or allowed in, every field pattern."""
    return base64.urlsafe_b64encode(raw).decode("ascii").rstrip("=")


def b64url_decode(encoded: str) -> bytes:
    """Restores the padding base64url dropped. Raises `binascii.Error` on
    anything that is not base64url, which callers treat as a rejected request
    rather than a crash."""
    return base64.urlsafe_b64decode(encoded + "=" * (-len(encoded) % 4))
