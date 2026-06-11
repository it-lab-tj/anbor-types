from enum import IntEnum


class CategoryKind(IntEnum):
    PRODUCT = 1
    OFFER = 2


class CatalogEntryKindEnum(IntEnum):
    PRODUCT = 1
    SERVICE = 2
    OFFER = 3


class BusinessOrientationEnum(IntEnum):
    ALL = 1
    PRODUCT = 2
    SERVICE = 3
