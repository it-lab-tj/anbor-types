from typing import Optional

from anbor_types.catalog.catalog_entry.results import CatalogEntryCreateResult


class ProductCreateResult(CatalogEntryCreateResult):
    """Result after product creation."""

    shelf_number: Optional[str] = None
    image: dict
