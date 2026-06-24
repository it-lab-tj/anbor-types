from anbor_types.catalog.catalog_entry.dto import (
    CatalogEntryCreateDTO,
    CatalogEntryListDTO,
    CatalogEntryUpdateDTO,
    CatalogEntryDetailedDTO,
)


class ServiceListDTO(CatalogEntryListDTO): ...


class ServiceDetailedDTO(CatalogEntryDetailedDTO): ...


class ServiceCreateDTO(CatalogEntryCreateDTO): ...


class ServiceUpdateDTO(CatalogEntryUpdateDTO): ...
