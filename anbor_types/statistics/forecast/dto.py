from decimal import Decimal
from typing import List

import msgspec

from anbor_types import ID_T
from anbor_types.catalog.category.dto import CharacteristicValuePairDTO
from anbor_types.common.dto import NameIdDTO


class ProductForecastEntryDTO(msgspec.Struct):
    """Product a purchase suggestion is for. ``characteristic_values`` expands the
    sold variant's characteristic→value pairs; empty when the product has no
    variant."""

    id: ID_T
    name: str
    # The unit the sibling quantities are counted in, so a `recommend_to_buy`
    # of 3 reads as 3 pieces or 3 kilograms. `name` is the short form
    # (`шт`, `кг`), as everywhere else this DTO is used.
    measurement_unit: NameIdDTO
    characteristic_values: List[CharacteristicValuePairDTO]


class ProductPurchaseSuggestionDTO(msgspec.Struct):
    entry: ProductForecastEntryDTO
    forecast_demand: Decimal  # forecast sales over the chosen horizon
    current_stock: Decimal
    snapshot_stock: Decimal  # remains on hand (mview refresh-time snapshot)
    recommend_to_buy: Decimal  # max(0, forecast_demand - current_stock)
