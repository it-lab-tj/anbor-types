import datetime
from typing import Optional

import msgspec

from anbor_types import ID_T, BasePydanticModel
from anbor_types.catalog.annotated import ATCatalogEntryDescription, ATCatalogEntryName, ATInformationStr
from anbor_types.common.annotated import ATDiscount, ATPrice


class CatalogEntryListDTO(msgspec.Struct):
    id: ID_T
    name: str
    updated_at: datetime
    slug: str


class CatalogEntryCreateDTO(BasePydanticModel):
    name: ATCatalogEntryName

    minimum_price: ATPrice
    selling_price: ATPrice
    max_discount: ATDiscount

    description: Optional[ATCatalogEntryDescription] = None
    information: Optional[ATInformationStr] = None

    # Non-validate
    category_id: ID_T
    measurement_unit_id: ID_T
    currency_id: ID_T