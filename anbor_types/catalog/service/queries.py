from anbor_types import Query, ID_T
from anbor_types.catalog.catalog_entry.queries import CatalogEntryBaseListQuery


class ServiceDetailedQuery(Query):
    id: ID_T


class ServiceListQuery(CatalogEntryBaseListQuery): ...
