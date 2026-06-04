from enum import IntEnum


class CategoryKind(IntEnum):
    PRODUCT = 1
    OFFER = 2


class CatalogEntryKindEnum(IntEnum):
    BASE = 3
    PRODUCT = 1
    OFFER = 2
    SERVICE = 4