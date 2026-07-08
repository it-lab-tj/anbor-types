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
    CatalogEntryDetailedDTO,
    CatalogEntryProfileListDTO,
)
from anbor_types.catalog.category.dto import CharValueDTO
from anbor_types.catalog.constraints import CATALOG_ENTRY_VARIANT_CHAR_VALUES_MAX_COUNT
from anbor_types.catalog.product.constraints import IMAGES_MAX_COUNT, PROFILES_MAX_COUNT
from anbor_types.common.annotated import ATPrice
from anbor_types.common.dto import NameDTO
from anbor_types.gallery.dto import ImageListDTO


class ProductSubjectRemainsListDTO(msgspec.Struct):
    subject: NameDTO
    remains: Decimal


# ===== PRODUCT PROFILE =====
class CatalogEntryProfileCreateDTO(BasePydanticModel):
    identifier: annotated.ATProductProfileIdentifier
    char_values: Optional[annotated.ATProductProfileCharValues] = Field(
        default_factory=list,
        max_length=CATALOG_ENTRY_VARIANT_CHAR_VALUES_MAX_COUNT,
    )


class ProductProfileUpsertDTO(CatalogEntryProfileCreateDTO):
    id: Optional[ID_T] = None


# ===== PRODUCT =====


class ProductListDTO(CatalogEntryListDTO):
    buying_price: Decimal
    shelf_number: str
    vendor_code: str
    remains: Decimal


class ProductCreateDTO(CatalogEntryCreateDTO):
    shelf_number: Optional[annotated.ATProductShelfNumber] = None

    consider_characteristics: bool
    buying_price: ATPrice
    surcharge: ATPrice

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
    files: Annotated[
        List[ID_T],
        Field(default_factory=list),
    ]


class ProductDetailedListDTO(msgspec.Struct):
    id: ID_T
    name: str
    selling_price: Decimal
    category_id: ID_T
    remains: Decimal
    images: List[ImageListDTO]
    description: Optional[str]
    information: Optional[str]
    profiles: List[CatalogEntryProfileListDTO]


class ProductRemainsRequestDTO(BasePydanticModel):
    storage_id: Optional[ID_T] = None
    char_values: List[CharValueDTO] = Field(
        default_factory=list,
        max_length=CATALOG_ENTRY_VARIANT_CHAR_VALUES_MAX_COUNT,
    )


class ProductRemainsDTO(msgspec.Struct):
    total: Decimal
    # Populated only when the corresponding filter was sent.
    storage_remains: Optional[Decimal] = None
    variant_remains: Optional[Decimal] = None


class ProductDetailedDTO(CatalogEntryDetailedDTO):
    buying_price: Decimal
    vendor_code: str
    remains: Decimal
    surcharge: Decimal
    consider_characteristics: bool
    shelf_number: Optional[str]

    subjects_remains: List[ProductSubjectRemainsListDTO]
    profiles: List[CatalogEntryProfileListDTO]
