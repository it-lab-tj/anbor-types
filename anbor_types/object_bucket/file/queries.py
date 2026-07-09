from anbor_types import ID_T, ListQuery, Query


class FileListQuery(ListQuery): ...


class FileByIdQuery(Query):
    id: ID_T
