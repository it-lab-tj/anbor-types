from pydantic import Field

from anbor_types import ListQuery


class CategoryListQuery(ListQuery):
    limit: int = Field(default=100000)
