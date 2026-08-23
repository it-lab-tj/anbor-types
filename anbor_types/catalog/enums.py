from enum import IntEnum, StrEnum


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


class CharacteristicKindEnum(StrEnum):
    """Input type of a category characteristic.

    Mirrors the legacy ``CategoryCharacteristic.TYPE`` choices, which is what
    the ``handbook_categorycharacteristic.kind`` column already holds; the
    catalog-entry import path writes ``CHAR``.
    """

    CHAR = "char"
    TEXT = "text"
    SELECT = "select"
    BOOLEAN = "boolean"
    CHECKBOX = "checkbox"
    DATE = "date"
    TIME = "time"
    NUMBER = "number"
