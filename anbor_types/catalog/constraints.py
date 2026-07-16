import regex

CATALOG_ENTRY_VARIANT_CHAR_VALUES_MAX_COUNT = 15


# VENDOR CODE
VENDOR_CODE_MAX_LENGTH = 24
VENDOR_CODE_MIN_LENGTH = 5

VENDOR_CODE_REGEX = regex.compile(r"^[\p{IsCyrillic}\p{IsLatin}0-9 _\-\(\)/]+$")


# MEASUREMENT UNIT (name, e.g. for import resolution / get-or-create)
MEASUREMENT_UNIT_NAME_MIN_LENGTH = 1
MEASUREMENT_UNIT_NAME_MAX_LENGTH = 50


# CHAR VALUE PAIR (one "characteristic:value" token in an import cell)
CHAR_VALUE_PAIR_MIN_LENGTH = 1
CHAR_VALUE_PAIR_MAX_LENGTH = 100


# CATEGORY (max depth of a "Parent; child; grand-child" path on import)
CATEGORY_MAX_DEPTH = 10
