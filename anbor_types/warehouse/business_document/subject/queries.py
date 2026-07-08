from typing import Annotated

from anbor_types import ID_T, ListQuery, Query
from anbor_types.api.filter_specs import AFStatus
from anbor_types.api.queries import ShortListQuery
from anbor_types.warehouse.constants.enums import SubjectKindEnum
from anbor_types.utils.filter.types import FilterSpec


class SubjectListQuery(ListQuery):
    kind: Annotated[
        SubjectKindEnum,
        FilterSpec.enum(
            SubjectKindEnum,
            description="**1** - Склад\n" "**2** - Клиент\n" "**3** - Исполнитель\n",
        ),
    ]
    status: AFStatus


class SubjectShortListQuery(ShortListQuery):
    kind: Annotated[
        SubjectKindEnum,
        FilterSpec.enum(
            SubjectKindEnum,
            description="**1** - Склад\n" "**2** - Клиент\n" "**3** - Исполнитель\n",
        ),
    ]


class SubjectDetailedQuery(Query):
    id: ID_T


class SubjectBalanceQuery(Query):
    id: ID_T


class SubjectStockProductsQuery(Query):
    id: ID_T
