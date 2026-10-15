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
    source_inventory_id: Optional[ID_T] = None
    """The lot this one was split off, for a TRANSFER_IN leg.

    A transfer receives ONE destination lot per source lot it consumed, each at
    that source lot's own price, so the destination keeps the cost structure of
    the shelf it came from instead of collapsing it into an average. This is the
    link back, and it is what lets an upstream reprice reach the right
    destination lot: they all share one ``document_item_id``, so the line alone
    cannot tell them apart.

    NULL for every other receipt kind -- a purchase or an adjustment increase
    creates stock rather than moving it, so there is no source lot.
    """
