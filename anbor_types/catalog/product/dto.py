from decimal import Decimal
from typing import Annotated, List, Optional, Tuple

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


# ===== PRODUCT DETAILED LIST (marketplace sync) =====
# The detailed list route exists only to feed the marketplace catalog sync, so it
# carries its own nested structs instead of the shared catalog-entry ones. The
# consumer joins the media root onto its own host and resolves characteristic
# values by id against its local copy, so the shape here must stay put even when
# the internal catalog-entry routes change.


class ProductDetailedListImageDTO(msgspec.Struct):
    """Image of a product, addressed relative to the media root.

    ``original_url`` is the stored path (``images/<uuid>.jpg``) rather than a
    full URL: the consumer prefixes it with the ERP host it synced from.
    """

    id: ID_T
    name: str
    original_url: str


class ProductDetailedListCharValueDTO(msgspec.Struct):
    """A single characteristic/value pair of a product profile."""

    characteristic_id: ID_T
    value_id: ID_T


class ProductDetailedListProfileDTO(msgspec.Struct):
    id: ID_T
    char_values: List[ProductDetailedListCharValueDTO]


class ProductDetailedListDTO(msgspec.Struct):
    id: ID_T
    name: str
    selling_price: Decimal
    category_id: ID_T
    remains: Decimal
    images: List[ProductDetailedListImageDTO]
    description: Optional[str]
    information: Optional[str]
    profiles: List[ProductDetailedListProfileDTO]


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

    subjects_remains: Tuple[ProductSubjectRemainsListDTO, ...]
    profiles: Tuple[CatalogEntryProfileListDTO, ...]


class CatalogEntryPositionListDTO(msgspec.Struct):
    id: ID_T
    variant_id: Optional[ID_T]
    name: str
    slug: str
    identifier: str
    kind: CatalogEntryKindEnum
    images: Tuple[CatalogEntryImageListDTO, ...] = msgspec.field(default_factory=list)
    remains: Optional[Decimal] = None
    selling_price: Optional[Decimal] = None
    minimum_price: Optional[Decimal] = None
    characteristics: Tuple[CharacteristicValuePairDTO, ...] = msgspec.field(
        default_factory=list
    )
