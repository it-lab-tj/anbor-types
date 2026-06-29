from anbor_types import ID_T, Query


class TransferDocumentGetQuery(Query):
    id: ID_T


class TransferDocumentGetDetailedQuery(Query):
    id: ID_T
