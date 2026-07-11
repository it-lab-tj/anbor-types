from typing import Annotated

from pydantic import Field

from anbor_types import ID_T, ListQuery, Query
from anbor_types.api.types import OrderingAllowedFieldsT
from anbor_types.catalog.enums import CategoryKindEnum
from anbor_types.utils.filter.meta import FilterMeta
from anbor_types.utils.filter.types import FilterSpec
from anbor_types.utils.mixins import OrderingQueryMixin


class CategoryListQuery(ListQuery):
    limit: int = Field(default=100000)


class CategoryCharacteristicsQuery(Query):
    category_id: ID_T


class CategoryShortListQuery(ListQuery, OrderingQueryMixin, metaclass=FilterMeta):
    _ordering_allowed_fields: OrderingAllowedFieldsT = {
        "created_at",
    }

    kind: Annotated[
        CategoryKindEnum,
        FilterSpec.enum(
            CategoryKindEnum,
            description="**1** - Товар\n" "**2** - Услуга\n",
        ),
    ]
