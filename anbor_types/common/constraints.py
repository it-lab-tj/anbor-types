from datetime import datetime, timezone
from decimal import Decimal

import regex


from anbor_types.api.constants import DECIMAL_ZERO, TITLE_REGEX
from anbor_types import Numeric

TITLE_REGEX = TITLE_REGEX


# NAME
NAME_MAX_LENGTH = 300
NAME_MIN_LENGTH = 3

NAME_REGEX = TITLE_REGEX


# SLUG
SLUG_MAX_LENGTH = 300

# INFORMATION
INFORMATION_MAX_LENGTH = 5000
COMMENT_MAX_LENGTH = 2000

# DESCRIPTION
DESCRIPTION_MAX_LENGTH = 5000

# DISCOUNTS
DISCOUNT_MAX = Decimal("100")
DISCOUNT_MIN = DECIMAL_ZERO

# PRICE
ANY_PRICE_MIN = DECIMAL_ZERO


# ==== =====


DECIMAL_BALANCE_DIGITS = 30
DECIMAL_BALANCE_PLACES = 4

LONG_DECIMAL_DIGITS = 30
LONG_DECIMAL_PLACES = 4

DECIMAL_PRICE_DIGITS = 14
DECIMAL_PRICE_PLACES = 4

DECIMAL_RATE_DIGITS = 12
DECIMAL_RATE_PLACES = 6

MAX_RATE = Decimal("100000")
MIN_RATE = Decimal("0.0001")


def ROUND_PRICE[T: Numeric](v: T) -> T:
    return round(v, DECIMAL_PRICE_PLACES)


DECIMAL_DISCOUNT_DIGITS = 5
DECIMAL_DISCOUNT_PLACES = 2


# ===== DATE & DATETIME =====
DATETIME_MAX = datetime(
    2080,
    1,
    1,
    23,
    59,
    59,
    tzinfo=timezone.utc,
)

DATETIME_MIN = datetime(
    2000,
    1,
    1,
    00,
    00,
    00,
    tzinfo=timezone.utc,
)

FILE_IDS_MAX_COUNT = 15

CONTENT_TYPE_MAX_LENGTH = 20

# ADDRESS
ADDRESS_MAX_LENGTH = 255
# TOFIX: matches exactly one character under `fullmatch` -- would reject every
# real address if the validator were enabled.
ADDRESS_REGEX = regex.compile(r"^[\w\s.,/№#-]$")

# PASSWORD
PASSWORD_MIN_LENGTH = 8
PASSWORD_MAX_LENGTH = 200


DECIMAL_AMOUNT_DIGITS = 14
DECIMAL_AMOUNT_PLACES = 4

# APP
APP_VERSION_REGEX = regex.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)\Z")

MAX_FILE_SIZE = 5  # MB
