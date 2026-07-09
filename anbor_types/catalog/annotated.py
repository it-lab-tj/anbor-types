from typing import Annotated, Optional

from pydantic import constr, conlist

from anbor_types import ID_T
from anbor_types.catalog.category.dto import CharValueDTO
from anbor_types.catalog.product import constraints as product_constraints
from anbor_types.catalog import constraints as catalog_enty_constraints
from anbor_types.common import constraints as common_constraints
from anbor_types.common.annotated import ATSingleLineStr

# ===== BASE =====
type ATCatalogEntryName = Annotated[
    ATSingleLineStr,
    constr(
        max_length=common_constraints.NAME_MAX_LENGTH,
        min_length=common_constraints.NAME_MIN_LENGTH,
        pattern=common_constraints.NAME_REGEX,
    ),
]
type ATCatalogEntryDescription = Annotated[
    Optional[ATSingleLineStr],
    constr(max_length=common_constraints.DESCRIPTION_MAX_LENGTH),
]


# ===== PRODUCT =====
type ATProductProfileIdentifier = Annotated[
    str,
    constr(
        max_length=product_constraints.PROFILE_IDENTIFIER_MAX_LENGTH,
        min_length=product_constraints.PROFILE_IDENTIFIER_MIN_LENGTH,
        pattern=product_constraints.PROFILE_IDENTIFIER_REGEX,
        strip_whitespace=True,
    ),
]
type ATProductProfileCharValues = Annotated[
    list[CharValueDTO],
    conlist(
        item_type=CharValueDTO,
        max_length=product_constraints.PROFILES_MAX_COUNT,
    ),
]
type ATCatalogEntryVendorCode = Annotated[
    str,
    constr(
        max_length=catalog_enty_constraints.VENDOR_CODE_MAX_LENGTH,
        min_length=catalog_enty_constraints.VENDOR_CODE_MIN_LENGTH,
        pattern=catalog_enty_constraints.VENDOR_CODE_REGEX,
        strip_whitespace=True,
    ),
]
type ATProductShelfNumber = Annotated[
    str,
    constr(
        max_length=product_constraints.SHELF_NUMBER_MAX_LENGTH,
        min_length=product_constraints.SHELF_NUMBER_MIN_LENGTH,
        pattern=product_constraints.SHELF_NUMBER_REGEX,
        strip_whitespace=True,
    ),
]
type ATProductImages = Annotated[
    list[ID_T], conlist(item_type=ID_T, max_length=product_constraints.IMAGES_MAX_COUNT)
]

# ====== FILE =======

type ATFileName = Annotated[
    ATSingleLineStr,
    constr(
        max_length=common_constraints.NAME_MAX_LENGTH,
        min_length=common_constraints.NAME_MIN_LENGTH,
        pattern=common_constraints.NAME_REGEX,
    ),
]
