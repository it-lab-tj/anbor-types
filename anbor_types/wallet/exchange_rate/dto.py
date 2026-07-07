from decimal import Decimal

import msgspec

from anbor_types import ID_T
from anbor_types.wallet.currency.dto import CurrencyShortDTO


class ExchangeRateShortDTO(msgspec.Struct):
    id: ID_T
    rate: Decimal
    target_currency: CurrencyShortDTO
