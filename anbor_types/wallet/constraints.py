from decimal import Decimal

SUBJECT_BALANCE_MAX = Decimal("99_999_999_999_999.9999")
SUBJECT_BALANCE_MIN = Decimal("-99_999_999_999_999.9999")


# OPERATION
OPERATION_COMMENT_MAX_LENGTH = 2000

# CASH DESK
# TODO: same limit as CASH_DESK_TITLE_MAX_LENGTH in cash_desk/constraints.py --
# one of the two names should win.
CASH_DESK_NAME_MAX_LENGTH = 100
