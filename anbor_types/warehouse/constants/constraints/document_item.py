from decimal import Decimal

from anbor_types.api import constants as api_constants

COUNT_MAX = Decimal("1_000_000")
COUNT_MIN = Decimal("0.01")

# TODO: alias kept only because the backend's document-item validation profile
# imports it; switch that import to anbor_types.api.constants, then delete this.
PRICE_MAX = api_constants.PRICE_MAX
PRICE_MIN = Decimal("0.0001")

DISCOUNT_MIN = Decimal("0.1")

CHAR_VALUES_MAX_COUNT = 15
