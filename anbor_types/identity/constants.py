from enum import IntEnum


class OtpKindEnum(IntEnum):
    """What a one-time code is *for*.

    Values are append-only — they are persisted in ``accounts_otp.kind`` and
    pinned by a CHECK constraint, so renumbering would silently reinterpret
    existing rows.
    """

    EMAIL_CONFIRMATION = 1
    PHONE_CONFIRMATION = 2
    FORGOT_PASSWORD = 3
    INVITATION = 4
