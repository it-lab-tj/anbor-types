from decimal import Decimal
from typing import List

import msgspec

from anbor_types import ID_T
from anbor_types.catalog.category.dto import CharacteristicValuePairDTO


class ProductForecastEntryDTO(msgspec.Struct):
    """Product a purchase suggestion is for. ``characteristic_values`` expands the
    sold variant's characteristic→value pairs; empty when the product has no
    variant."""

    id: ID_T
    name: str
    characteristic_values: List[CharacteristicValuePairDTO]


class ProductPurchaseSuggestionDTO(msgspec.Struct):
    entry: ProductForecastEntryDTO
    forecast_demand: Decimal  # forecast sales over the chosen horizon
    current_stock: Decimal  # remains on hand (mview refresh-time snapshot)
    recommend_to_buy: Decimal  # max(0, forecast_demand - current_stock)
