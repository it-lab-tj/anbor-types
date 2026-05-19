from enum import IntEnum


class BusinessDocumentActionEnum(IntEnum):
    SALE = 0
    PURCHASE = 1
    TRANSFER = 2
    RETURN_IN = 3
    RETURN_OUT = 4
    INVOICE = 5
    WRITE_OFF = 6
    ADJUSTMENT = 7


class BusinessDocumentApplicationStatusEnum(IntEnum):
    PENDING = 1
    REJECTED = 2
    CONFIRMED = 3


class AdjustmentDocumentKindEnum(IntEnum):
    WRITE_OFF = 0
    INVOICE = 1
    HYBRID = 2


class CounterpartyKind(IntEnum):
    STORAGE = 1
    CLIENT = 2
