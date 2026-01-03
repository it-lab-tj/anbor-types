from enum import IntEnum


class HandshakeKindEnum(IntEnum):
    MARKETPLACE = 1


class HandshakeStatusEnum(IntEnum):
    PENDING = 1
    EXPIRED = 2
    CONFIRMED = 3
    REJECTED = 4
