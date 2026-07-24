from decimal import Decimal
from typing import Optional

import msgspec


class ProductPurchaseSuggestionDTO(msgspec.Struct):
    product_id: int
    variant_id: Optional[int]  # None when the product has no variant
    forecast_demand: Decimal  # forecast sales over the chosen horizon
    current_stock: Decimal  # remains on hand (mview refresh-time snapshot)
    recommend_to_buy: Decimal  # max(0, forecast_demand - current_stock)
