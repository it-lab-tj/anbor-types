from enum import IntEnum


class BusinessDocumentActionEnum(IntEnum):
    SALE = 0
    PURCHASE = 1
    TRANSFER = 2
    RETURN_IN = 3
    RETURN_OUT = 4
    ADJUSTMENT = 5
    SERVICE = 6


class BusinessDocumentApplicationStatusEnum(IntEnum):
    PENDING = 0
    CONFIRMED = 1
    REJECTED = 2


class AdjustmentDocumentKindEnum(IntEnum):
    WRITE_OFF = 0
    INVOICE = 1
    HYBRID = 2


class SubjectKindEnum(IntEnum):
    STORAGE = 1
    CLIENT = 2
    INTERNAL = 3
    EXECUTOR = 4


class DocumentItemExtKindEnum(IntEnum):
    CONSUME = 0
    SOURCE = 1
    RETURN = 2


class InventoryAllocationStrategyEnum(IntEnum):
    FIFO = 1
    LIFO = 2
    FEFO = 3
    AVERAGE = 4
