from anbor_types import ID_T, Query


class PurchaseDocumentGetQuery(Query):
    id: ID_T


class PurchaseDocumentGetDetailedQuery(Query):
    id: ID_T
