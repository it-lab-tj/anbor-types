from typing import Annotated, List

from pydantic import Field

from anbor_types import ID_T
from anbor_types.catalog.catalog_entry.dto import (
    CatalogEntryCreateDTO,
    CatalogEntryListDTO,
    CatalogEntryUpdateDTO,
    CatalogEntryDetailedDTO,
)
from anbor_types.catalog.product.constraints import IMAGES_MAX_COUNT


class ServiceListDTO(CatalogEntryListDTO): ...


class ServiceDetailedDTO(CatalogEntryDetailedDTO): ...


class ServiceCreateDTO(CatalogEntryCreateDTO): ...


class ServiceUpdateDTO(CatalogEntryUpdateDTO):
    files: Annotated[
        List[ID_T],
        Field(default_factory=list),
    ]
    images: Annotated[
        List[ID_T],
        Field(default_factory=list, max_length=IMAGES_MAX_COUNT),
    ]
