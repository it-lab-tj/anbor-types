from decimal import Decimal
from typing import Annotated, List, Optional

import msgspec
from pydantic import conlist, Field

from anbor_types import ID_T, BasePydanticModel
from anbor_types.api.constants import DECIMAL_ZERO
from anbor_types.catalog import annotated
from anbor_types.catalog.catalog_entry.dto import (
    CatalogEntryCreateDTO,
    CatalogEntryImageListDTO,
    CatalogEntryListDTO,
    CatalogEntryUpdateDTO,
    CatalogEntryDetailedDTO,
    CatalogEntryProfileListDTO,
)
from anbor_types.catalog.category.dto import (
    CharValueDTO,
    CharacteristicValuePairDTO,
)
from anbor_types.catalog.constraints import CATALOG_ENTRY_VARIANT_CHAR_VALUES_MAX_COUNT
from anbor_types.catalog.enums import CatalogEntryKindEnum
from anbor_types.catalog.product.constraints import IMAGES_MAX_COUNT, PROFILES_MAX_COUNT
from anbor_types.common.annotated import ATPrice
from anbor_types.common.dto import NameDTO


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


class ProductProfileCharacteristicsDTO(msgspec.Struct):
    identifier: str
    characteristics: List[CharacteristicValuePairDTO]


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
    # Defaulted (pydantic does not validate defaults) so imports that don't carry
    # a markup can omit it; explicit values still go through ATPrice.
    surcharge: ATPrice = DECIMAL_ZERO

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
    images: List[CatalogEntryImageListDTO]
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


class CatalogEntryPositionsListDTO(msgspec.Struct):
    id: ID_T
    variant_id: Optional[ID_T]
    name: str
    slug: str
    identifier: str
    kind: CatalogEntryKindEnum
    images: List[CatalogEntryImageListDTO] = msgspec.field(default_factory=list)
    selling_price: Optional[Decimal] = None
    minimum_price: Optional[Decimal] = None
    characteristics: List[CharacteristicValuePairDTO] = msgspec.field(
        default_factory=list
    )
