from enum import StrEnum


class FilterLookupEnum(StrEnum):
    EQ = "eq"
    GT = "gt"
    LT = "lt"
    GTE = "gte"
    LTE = "lte"
    IN = "in"
    RANGE = "rn"
    SEARCH = "search"
