from datetime import datetime
from decimal import Decimal
from typing import Annotated, Optional

from pydantic import StringConstraints

from anbor_types import ID_T, ListQuery
from anbor_types.common.constraints import DATETIME_MAX
from anbor_types.common.enums import StatusEnum
from anbor_types.utils.filter.meta import FilterMeta, FilterSpec
from src.app.shared_kernel.constants.entity_common_constraints import ID_MAX, PRICE_MAX
from anbor_types.api.annotated import AFSearch


class CatalogEntryBaseListQuery(ListQuery, metaclass=FilterMeta):
    search: Optional[AFSearch] = None

    measurement_unit_id: Annotated[
        ID_T,
        FilterSpec.numeric(
            int,
            lte=ID_MAX,
        ),
    ]

    currency_id: Annotated[
        ID_T,
        FilterSpec.numeric(
            int, lte=ID_MAX, description="Test description with `Markdown`"
        ),
    ]

    status: Annotated[
        StatusEnum,
        FilterSpec.numeric(
            StatusEnum,
            choices=StatusEnum,
        ),
    ]

    selling_price: Annotated[
        Decimal,
        FilterSpec.numeric_range(
            Decimal,
            lte=PRICE_MAX,
            gt=Decimal("0"),
        ),
    ]

    minimum_price: Annotated[
        Decimal,
        FilterSpec.numeric_range(
            Decimal,
            lte=PRICE_MAX,
            gt=Decimal("0"),
        ),
    ]

    created_at: Annotated[
        datetime,
        FilterSpec.datetime_range(
            lte=DATETIME_MAX,
        ),
    ]

    type ATOrdering = Annotated[
        str,
        StringConstraints(
            max_length=100,
        ),
    ]
