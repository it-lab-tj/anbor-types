from datetime import datetime, date
from decimal import Decimal
from typing import Optional

import msgspec

from anbor_types import ID_T


class InventoryCreateDTO(msgspec.Struct):
    product_id: ID_T
    document_item_id: ID_T
    storage_id: ID_T
    remains: Decimal
    price: Decimal
    variant_id: Optional[ID_T] = None
    shipped_at: Optional[datetime] = None
    expires_at: Optional[date] = None
