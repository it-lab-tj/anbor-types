from enum import IntEnum


class CategoryKindEnum(IntEnum):
    PRODUCT = 1
    SERVICE = 2


class CatalogEntryKindEnum(IntEnum):
    PRODUCT = 1
    SERVICE = 2


class BusinessOrientationEnum(IntEnum):
    ALL = 1
    PRODUCT = 2
    SERVICE = 3
