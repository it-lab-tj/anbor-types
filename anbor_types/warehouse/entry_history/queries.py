from decimal import Decimal
from typing import Annotated, List, Tuple

from anbor_types import ID_T, ListQuery
from anbor_types.api.constants import ID_MAX
from anbor_types.api.types import OrderingAllowedFieldsT
from anbor_types.catalog.category.dto import CharValueDTO
from anbor_types.common.annotated import ATDatetimeRN
from anbor_types.utils.filter.meta import FilterMeta
from anbor_types.utils.filter.types import FilterSpec
from anbor_types.utils.mixins import OrderingQueryMixin
from anbor_types.warehouse.constants.constraints.document_item import (
    CHAR_VALUES_MAX_COUNT,
    COUNT_MAX,
    PRICE_MAX,
)
from anbor_types.warehouse.constants.enums import BusinessDocumentActionEnum


class CatalogEntryHistoryListQuery(ListQuery, OrderingQueryMixin, metaclass=FilterMeta):
    """Movement history of one catalog entry -- product or service -- across
    every business document that referenced it.

    `entry_id` comes from the URL path, not from query params.

    Only confirmed documents appear. Returns (RETURN_IN / RETURN_OUT) are
    excluded: they carry no subject, currency or project of their own, so they
    would render as empty rows next to the document they reverse.

    The subject filters are role-based, not column-based -- which column carries
    the concept depends on the document's action. `client_id` matches the
    counterparty side (credit on purchase, debit on sale, counterparty on
    service); `storage_id` matches the stock side (debit on purchase, credit on
    sale, performer on service, storage on adjustment, either side on transfer).
    """

    _ordering_allowed_fields: OrderingAllowedFieldsT = {
        "name",
        "vendor_code",
        "count",
        "price",
        "amount",
        "shipped_at",
    }

    # Comes from the URL path, not from query params.
    entry_id: ID_T

    action: Annotated[
        BusinessDocumentActionEnum,
        FilterSpec.enum(
            BusinessDocumentActionEnum,
            description="**0** - Продажа\n"
            "**1** - Закупка\n"
            "**2** - Перемещение\n"
            "**5** - Корректировка\n"
            "**6** - Услуга\n",
        ),
    ]

    client_id: Annotated[
        ID_T,
        FilterSpec.numeric(
            int,
            lte=ID_MAX,
            description="Counterparty side: credit on purchase, debit on sale, "
            "counterparty on service.",
        ),
    ]

    storage_id: Annotated[
        ID_T,
        FilterSpec.numeric(
            int,
            lte=ID_MAX,
            description="Stock side: debit on purchase, credit on sale, "
            "performer on service, storage on adjustment, either side on "
            "transfer.",
        ),
    ]

    created_by_id: Annotated[
        ID_T,
        FilterSpec.numeric(
            int, lte=ID_MAX, description="Author of the document *item*."
        ),
    ]

    project_id: Annotated[
        ID_T,
        FilterSpec.numeric(int, lte=ID_MAX),
    ]

    count__rn: Annotated[
        Tuple[Decimal, Decimal],
        FilterSpec.numeric_range(
            Decimal,
            gte=Decimal("0"),
            lte=COUNT_MAX,
        ),
    ]

    price__rn: Annotated[
        Tuple[Decimal, Decimal],
        FilterSpec.numeric_range(
            Decimal,
            gte=Decimal("0"),
            lte=PRICE_MAX,
        ),
    ]

    shipped_at__rn: ATDatetimeRN

    char_values: Annotated[
        List[CharValueDTO],
        FilterSpec.json(
            CharValueDTO,
            max_length=CHAR_VALUES_MAX_COUNT,
            description="JSON array of `{characteristic_id, value_id}`. Matches "
            "items whose variant carries *all* of the given pairs, so extra "
            "characteristics on the variant do not disqualify it.",
        ),
    ]
