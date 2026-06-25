from anbor_types import ID_T, Query


class AdjustmentDocumentGetQuery(Query):
    id: ID_T


class AdjustmentDocumentGetDetailedQuery(Query):
    id: ID_T
