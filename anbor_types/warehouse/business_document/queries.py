from decimal import Decimal
from typing import Annotated, Tuple

from pydantic import StringConstraints

from anbor_types import ID_T, ListQuery, Query
from anbor_types.api.constants import ID_MAX, PRICE_MAX
from anbor_types.catalog.enums import CatalogEntryKindEnum
from anbor_types.api.types import OrderingAllowedFieldsT
from anbor_types.common.annotated import ATDatetimeRN
from anbor_types.utils.filter import FilterLookupEnum
from anbor_types.utils.filter.meta import FilterMeta, FilterSpec
from anbor_types.utils.mixins import OrderingQueryMixin
from anbor_types.warehouse.constants.enums import (
    BusinessDocumentActionEnum,
    BusinessDocumentApplicationStatusEnum,
)


class BusinessDocumentListQuery(ListQuery, OrderingQueryMixin, metaclass=FilterMeta):
    """Unified business document list query.

    Subject/currency/project filters are document-specific: each action matches
    on the column that carries the concept (e.g. ``debit_id`` is the client for
    SALE, the storage for PURCHASE/ADJUSTMENT, the counterparty for SERVICE);
    returns resolve through their parent sale/purchase. Documents that lack the
    concept at all (ADJUSTMENT has no credit, TRANSFER has no currency/paid)
    simply never match that filter.
    """

    _ordering_allowed_fields: OrderingAllowedFieldsT = {
        "created_at",
        "shipped_at",
        "amount",
        "vendor_code",
    }

    # Matches vendor code or a debit/credit subject name prefix.
    # Declared as explicit Annotated (not the AFSearch alias): PEP-695 `type`
    # aliases hide the FilterSpec from FilterMeta/parse_filters, so the alias
    # form never reaches the compiler.
    search: Annotated[
        str,
        StringConstraints(max_length=100, strip_whitespace=True),
        FilterSpec.string(max_length=100),
    ]

    action: Annotated[
        BusinessDocumentActionEnum,
        FilterSpec.enum(BusinessDocumentActionEnum),
    ]

    action__in: Annotated[
        BusinessDocumentActionEnum,
        FilterSpec.collection(
            BusinessDocumentActionEnum,
            lookup=FilterLookupEnum.IN,
            required=False,
            choices=(
                BusinessDocumentActionEnum.SALE,
                BusinessDocumentActionEnum.SERVICE,
            ),
        ),
    ]

    application_status: Annotated[
        BusinessDocumentApplicationStatusEnum,
        FilterSpec.enum(BusinessDocumentApplicationStatusEnum),
    ]

    debit_id: Annotated[
        ID_T,
        FilterSpec.numeric(int, lte=ID_MAX),
    ]

    credit_id: Annotated[
        ID_T,
        FilterSpec.numeric(int, lte=ID_MAX),
    ]

    currency_id: Annotated[
        ID_T,
        FilterSpec.numeric(int, lte=ID_MAX),
    ]

    project_id: Annotated[
        ID_T,
        FilterSpec.numeric(int, lte=ID_MAX),
    ]

    # Matches documents created OR last updated by the given user.
    staff_member_id: Annotated[
        ID_T,
        FilterSpec.numeric(int, lte=ID_MAX),
    ]

    amount__rn: Annotated[
        Tuple[Decimal, Decimal],
        FilterSpec.numeric_range(
            Decimal,
            lte=PRICE_MAX,
            gt=Decimal("0"),
        ),
    ]

    paid: Annotated[
        Decimal,
        FilterSpec.numeric(
            Decimal,
            gte=Decimal("0"),
            lte=PRICE_MAX,
        ),
    ]

    paid__rn: Annotated[
        Tuple[Decimal, Decimal],
        FilterSpec.numeric_range(
            Decimal,
            lte=PRICE_MAX,
            gte=Decimal("0"),
        ),
    ]

    shipped_at__rn: ATDatetimeRN

    created_at__rn: ATDatetimeRN

    # When value is `True`, all documents which matching to expression `doc.amount == doc.paid`, otherwise all not payed
    is_paid: Annotated[
        bool,
        FilterSpec.boolean(
            required=False,
            description="When a document `paid > 0` - it's true. Otherwise, `paid == 0",
        ),
    ]


class BusinessDocumentGetDetailedQuery(Query):
    """Kind-agnostic detail fetch: resolves the document's kind from its id and
    returns that kind's detailed DTO."""

    id: ID_T


class DocumentEntryListQuery(ListQuery, metaclass=FilterMeta):
    """Catalog entry picker for document items (products + services)."""

    # Comes from the URL path, not from query params.
    subject_id: ID_T

    search: Annotated[
        str,
        StringConstraints(max_length=100, strip_whitespace=True),
        FilterSpec.string(max_length=100),
    ]

    kind: Annotated[
        CatalogEntryKindEnum,
        FilterSpec.enum(
            CatalogEntryKindEnum,
            description="**1** - Товар\n" "**2** - Услуга\n",
        ),
    ]
