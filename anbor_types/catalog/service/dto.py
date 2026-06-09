from decimal import Decimal
from datetime import datetime
from typing import Optional

import msgspec

from anbor_types import ID_T
from anbor_types.catalog.annotated import ATProductVendorCode
from anbor_types.catalog.catalog_entry.dto import (
    CatalogEntryCreateDTO,
    CatalogEntryListDTO,
    CatalogEntryUpdateDTO,
)


class ServiceListDTO(CatalogEntryListDTO):
    selling_price: Decimal
    vendor_code: Optional[str]
    measurement_unit: dict
    category: dict


class ServiceDetailedDTO(msgspec.Struct):
    id: ID_T
    name: str
    selling_price: Decimal
    minimum_price: Decimal
    vendor_code: Optional[str]
    description: Optional[str]
    information: Optional[str]
    category_id: ID_T
    measurement_unit_id: ID_T
    slug: str
    updated_at: datetime


class ServiceCreateDTO(CatalogEntryCreateDTO):
    vendor_code: ATProductVendorCode


class ServiceUpdateDTO(CatalogEntryUpdateDTO):
    vendor_code: ATProductVendorCode
