from decimal import Decimal


from anbor_types.common.constraints import TITLE_REGEX

DEFAULT_LIMIT = 10
DEFAULT_OFFSET = 0

MAX_LIMIT = 300
MIN_LIMIT = 1
MIN_OFFSET = 0

TITLE_MIN_LENGTH = 1
TITLE_MAX_LENGTH = 100

TITLE_REGEX = TITLE_REGEX


ID_MAX = 2**31 - 1  # 32 bits
PRICE_MAX = Decimal("9_999_999_999")
PRICE_GT = Decimal("0")
