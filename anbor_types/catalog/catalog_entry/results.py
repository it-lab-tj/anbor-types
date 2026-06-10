from datetime import datetime
from decimal import Decimal

from anbor_types import ID_T, BasePydanticModel


class CatalogEntryCreateResult(BasePydanticModel):
    """Shared payload returned by catalog entry create endpoints (product, service)."""

    id: ID_T
    name: str
    selling_price: Decimal
    updated_at: datetime
    category: dict
    measurement_unit: dict
