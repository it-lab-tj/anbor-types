from datetime import datetime
from decimal import Decimal
from typing import Optional, List, Annotated

import msgspec
from pydantic import Field

from anbor_types import ID_T, BasePydanticModel
from anbor_types.catalog.annotated import (
    ATCatalogEntryDescription,
    ATCatalogEntryName,
    ATCatalogEntryVendorCode,
)
from anbor_types.catalog.category.dto import CharValueDetailedDTO, CategoryShortDTO
from anbor_types.catalog.product.constraints import IMAGES_MAX_COUNT
from anbor_types.common.annotated import ATDiscount, ATPrice, ATInformationStr
from anbor_types.common.dto import NameIdDTO, FileShortDTO
from anbor_types.common.enums import StatusEnum
from anbor_types.gallery.dto import ImageShortDTO
from anbor_types.identity.user.dto import AuthorInfoShortDTO
from anbor_types.wallet.currency.dto import CurrencyShortDTO


class CatalogEntryProfileListDTO(msgspec.Struct):
    id: ID_T
    characteristic_values: List[CharValueDetailedDTO]
    identifier: str


class CatalogEntryListDTO(msgspec.Struct):
    id: ID_T
    name: str
    vendor_code: str
    minimum_price: Decimal
    selling_price: Decimal
    max_discount: Decimal
    slug: str
    description: Optional[str]
    information: Optional[str]
    image_url: Optional[str]  # Must be full url
    status: StatusEnum
    created_at: datetime

    currency: CurrencyShortDTO
    measurement_unit: NameIdDTO
    category: NameIdDTO


class CatalogEntryDetailedDTO(msgspec.Struct):
    id: ID_T
    name: str
    vendor_code: str
    minimum_price: Decimal
    selling_price: Decimal
    max_discount: Decimal
    description: Optional[str]
    information: Optional[str]
    created_at: datetime
    updated_at: datetime

    currency: CurrencyShortDTO
    measurement_unit: NameIdDTO
    category: CategoryShortDTO
    created_by: AuthorInfoShortDTO
    files: List[FileShortDTO]
    images: List[ImageShortDTO]


class CatalogEntryCreateDTO(BasePydanticModel):
    name: ATCatalogEntryName

    minimum_price: ATPrice
    selling_price: ATPrice
    max_discount: ATDiscount

    description: Optional[ATCatalogEntryDescription] = None
    information: Optional[ATInformationStr] = None
    vendor_code: ATCatalogEntryVendorCode

    # Non-validate
    category_id: ID_T
    measurement_unit_id: ID_T
    currency_id: ID_T
    images: Annotated[
        List[ID_T],
        Field(default_factory=list, max_length=IMAGES_MAX_COUNT),
    ]
    files: Annotated[
        List[ID_T],
        Field(default_factory=list, alias="file_ids"),
    ]


class CatalogEntryUpdateDTO(BasePydanticModel):
    name: ATCatalogEntryName

    minimum_price: ATPrice
    selling_price: ATPrice
    max_discount: ATDiscount
    vendor_code: ATCatalogEntryVendorCode

    description: Optional[ATCatalogEntryDescription] = None
    information: Optional[ATInformationStr] = None

    # Non-validate
    category_id: ID_T
    measurement_unit_id: ID_T
    currency_id: ID_T
