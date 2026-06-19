from decimal import Decimal
from typing import Annotated, List, Optional

import msgspec
from pydantic import conlist, Field

from anbor_types import ID_T, BasePydanticModel
from anbor_types.catalog import annotated
from anbor_types.catalog.catalog_entry.dto import (
    CatalogEntryCreateDTO,
    CatalogEntryListDTO,
    CatalogEntryUpdateDTO,
)
from anbor_types.catalog.category.dto import CharValuesListDTO
from anbor_types.catalog.constraints import CATALOG_ENTRY_VARIANT_CHAR_VALUES_MAX_COUNT
from anbor_types.catalog.product.constraints import IMAGES_MAX_COUNT, PROFILES_MAX_COUNT
from anbor_types.common.annotated import ATPrice
from anbor_types.common.dto import NameDTO
from anbor_types.gallery.dto import ImageListDTO, ImageOriginalUrlDTO
from anbor_types.wallet.currency.dto import CurrencyCodeSymbolDTO

# ===== PRODUCT PROFILE =====


class CatalogEntryProfileCreateDTO(BasePydanticModel):
    identifier: annotated.ATProductProfileIdentifier
    char_values: Optional[annotated.ATProductProfileCharValues] = Field(
        default_factory=list,
        max_length=CATALOG_ENTRY_VARIANT_CHAR_VALUES_MAX_COUNT,
    )


class ProductProfileUpsertDTO(CatalogEntryProfileCreateDTO):
    id: Optional[ID_T] = None


class CatalogEntryProfileListDTO(msgspec.Struct):
    id: ID_T
    characteristic_values: List[CharValuesListDTO]


# ===== PRODUCT =====


class ProductListDTO(CatalogEntryListDTO):
    buying_price: Decimal
    selling_price: Decimal
    minimum_price: Decimal
    vendor_code: str

    image: ImageOriginalUrlDTO
    measurement_unit: NameDTO
    category: NameDTO
    currency: CurrencyCodeSymbolDTO


class ProductCreateDTO(CatalogEntryCreateDTO):
    shelf_number: Optional[annotated.ATProductShelfNumber] = None

    consider_characteristics: bool
    buying_price: ATPrice
    surcharge: ATPrice
    images: Annotated[
        List[ID_T],
        Field(default_factory=list, max_length=IMAGES_MAX_COUNT),
    ]

    profiles: Annotated[
        Optional[List[CatalogEntryProfileCreateDTO]],
        conlist(
            item_type=CatalogEntryProfileCreateDTO,
            max_length=PROFILES_MAX_COUNT,
        ),
        Field(default_factory=list),
    ]


class ProductUpdateDTO(CatalogEntryUpdateDTO):
    buying_price: ATPrice
    surcharge: ATPrice
    shelf_number: Optional[annotated.ATProductShelfNumber] = None
    consider_characteristics: bool
    images: Annotated[
        List[ID_T],
        Field(default_factory=list, max_length=IMAGES_MAX_COUNT),
    ]

    profiles: Annotated[
        List[ProductProfileUpsertDTO],
        conlist(
            item_type=ProductProfileUpsertDTO,
            max_length=PROFILES_MAX_COUNT,
        ),
        Field(default_factory=list),
    ]


class ProductDetailedListDTO(msgspec.Struct):
    id: ID_T
    name: str
    selling_price: Decimal
    category_id: ID_T
    remains: Decimal
    images: List[ImageListDTO]
    profiles: List[CatalogEntryProfileListDTO]
    description: Optional[str]
    information: Optional[str]
