from pydantic import Field

from anbor_types import ID_T, ListQuery, Query


class CategoryListQuery(ListQuery):
    limit: int = Field(default=100000)


class CategoryCharacteristicsQuery(Query):
    category_id: ID_T
