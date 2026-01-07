from decimal import Decimal
from typing import Annotated, List, Optional

import msgspec
from pydantic import conlist, Field

from anbor_types import ID_T, BasePydanticModel
from anbor_types.catalog import annotated
from anbor_types.catalog.catalog_entry.dto import (
    CatalogEntryCreateDTO,
    CatalogEntryListDTO,
)
from anbor_types.catalog.product.constraints import IMAGES_MAX_COUNT, PROFILES_MAX_COUNT
from anbor_types.common import annotated as common_annotated
from anbor_types.gallery.dto import ImageListDTO


# ===== PRODUCT PROFILE =====


class ProductProfileCreateDTO(BasePydanticModel):
    identifier: annotated.ATProductProfileIdentifier
    char_values: Optional[annotated.ATProductProfileCharValues] = Field(
        default_factory=list
    )


# ===== PRODUCT =====


class ProductListDTO(CatalogEntryListDTO):
    buying_price: Decimal
    selling_price: Decimal
    minimum_price: Decimal
    vendor_code: str

    image: dict
    measurement_unit: dict
    category: dict


class ProductCreateDTO(CatalogEntryCreateDTO):
    vendor_code: annotated.ATProductVendorCode
    shelf_number: Optional[annotated.ATProductShelfNumber] = None

    consider_characteristics: bool
    buying_price: common_annotated.ATPrice
    surcharge: common_annotated.ATPrice
    images: Annotated[
        list[ID_T],
        Field(default_factory=list, max_length=IMAGES_MAX_COUNT),
    ]

    profiles: Annotated[
        Optional[List[ProductProfileCreateDTO]],
        conlist(
            item_type=ProductProfileCreateDTO,
            max_length=PROFILES_MAX_COUNT,
        ),
        Field(default_factory=list),
    ]


class ProductDetailedListDTO(msgspec.Struct):
    id: ID_T
    name: str
    description: str
    information: str
    selling_price: Decimal
    measurement_unit_name: str
    images: List[ImageListDTO]
