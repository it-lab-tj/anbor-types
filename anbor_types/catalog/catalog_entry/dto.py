from datetime import datetime
from decimal import Decimal
from typing import Optional, List, Annotated, Tuple

import msgspec
from pydantic import Field

from anbor_types import ID_T, BasePydanticModel
from anbor_types.api.constants import DECIMAL_ZERO
from anbor_types.catalog.annotated import (
    ATCatalogEntryDescription,
    ATCatalogEntryName,
    ATCatalogEntryVendorCode,
)
from anbor_types.catalog.category.dto import (
    CharacteristicValuePairDTO,
    CategoryShortDTO,
)
from anbor_types.catalog.product.constraints import IMAGES_MAX_COUNT
from anbor_types.common.annotated import ATDiscount, ATPrice, ATInformationStr
from anbor_types.common.dto import NameIdDTO, FileShortDTO
from anbor_types.common.enums import StatusEnum
from anbor_types.identity.user.dto import AuthorInfoShortDTO
from anbor_types.wallet.currency.dto import CurrencyShortDTO


class CatalogEntryImageListDTO(msgspec.Struct, omit_defaults=True):
    """Image of a catalog entry (product / service).

    A single struct shared by every catalog-entry-based response. ``id`` is
    always present; the URL fields are populated per-route and ``omit_defaults``
    drops the ones left unset (so a list route sends ``thumbnail``/``medium``
    while a detailed route sends ``original``). All URLs are full (host-qualified).
    """

    id: ID_T
    medium: Optional[str] = None
    thumbnail: Optional[str] = None
    original: Optional[str] = None


class CatalogEntryProfileListDTO(msgspec.Struct):
    id: ID_T
    identifier: str
    characteristic_values: Tuple[CharacteristicValuePairDTO, ...]


class CatalogEntryListDTO(msgspec.Struct):
    id: ID_T
    name: str
    vendor_code: str
    minimum_price: Decimal
    selling_price: Decimal
    max_discount: Decimal
    slug: str
    images: List[CatalogEntryImageListDTO]
    description: Optional[str]
    information: Optional[str]
    status: StatusEnum
    created_at: datetime

    currency: CurrencyShortDTO
    measurement_unit: NameIdDTO
    category: NameIdDTO


class CatalogEntryDetailedDTO(msgspec.Struct, kw_only=True):
    id: ID_T
    name: str
    vendor_code: str
    minimum_price: Decimal
    selling_price: Decimal
    measurement_units_ratio: Decimal
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
    images: List[CatalogEntryImageListDTO]

    second_measurement_unit: Optional[NameIdDTO] = None


class CatalogEntryOnBusinessDocumentItemDTO(msgspec.Struct):
    id: ID_T
    name: str
    selling_price: Decimal
    minimum_price: Decimal
    max_discount: Decimal
    images: List[CatalogEntryImageListDTO]
    currency: CurrencyShortDTO
    measurement_unit: NameIdDTO


class CatalogEntryCreateDTO(BasePydanticModel):
    name: ATCatalogEntryName

    minimum_price: ATPrice
    selling_price: ATPrice
    max_discount: ATDiscount

    # Non-validate
    category_id: ID_T
    measurement_unit_id: ID_T
    measurement_units_ratio: ATPrice = DECIMAL_ZERO
    currency_id: ID_T
    images: Annotated[
        List[ID_T],
        Field(default_factory=list, max_length=IMAGES_MAX_COUNT),
    ]
    files: Annotated[
        List[ID_T],
        Field(default_factory=list),
    ]

    second_measurement_unit_id: Optional[ID_T] = None
    description: Optional[ATCatalogEntryDescription] = None
    information: Optional[ATInformationStr] = None
    vendor_code: Optional[ATCatalogEntryVendorCode] = None


class CatalogEntryUpdateDTO(BasePydanticModel):
    name: ATCatalogEntryName

    minimum_price: ATPrice
    selling_price: ATPrice
    max_discount: ATDiscount
    vendor_code: Optional[ATCatalogEntryVendorCode] = None

    description: Optional[ATCatalogEntryDescription] = None
    information: Optional[ATInformationStr] = None

    # Non-validate
    category_id: ID_T
    measurement_unit_id: ID_T
    currency_id: ID_T
    second_measurement_unit_id: Optional[ID_T] = None
    measurement_units_ratio: ATPrice = DECIMAL_ZERO


class CatalogEntryImportAcceptedDTO(msgspec.Struct):
    """Result of a catalog-entry import (synchronous run)."""

    file_ref: str
    status: str = "completed"
    created_count: int = 0
