from decimal import Decimal
from typing import Optional

from anbor_types.catalog.catalog_entry.results import CatalogEntryCreateResult
from anbor_types.common.enums import StatusEnum


class ProductCreateResult(CatalogEntryCreateResult):
    """Result after product creation."""

    shelf_number: Optional[str] = None
    buying_price: Decimal
    selling_price: Decimal
    minimum_price: Decimal
    max_discount: Decimal
    status: StatusEnum
    image: dict
    remains: Decimal
    vendor_code: str