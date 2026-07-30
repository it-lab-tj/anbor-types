from datetime import date
from decimal import Decimal
from typing import List, Optional

from pydantic import Field, model_validator

from anbor_types import ID_T, BasePydanticModel, ListQuery, Query
from anbor_types.api.types import OrderingAllowedFieldsT
from anbor_types.catalog.category.dto import CharValueDTO
from anbor_types.common.annotated import ATRate
from anbor_types.common.enums import StatusEnum
from anbor_types.utils.filter.meta import FilterMeta
from anbor_types.utils.mixins import OrderingQueryMixin
from anbor_types.warehouse.constants.constraints import (
    document as doc_constraints,
    document_item as item_constraints,
)


class SaleDocumentListQuery(ListQuery):
    status: Optional[StatusEnum] = None


class SaleDocumentGetQuery(Query):
    id: ID_T


class SaleDocumentGetDetailedQuery(Query):
    id: ID_T


class SaleProfitDocumentItemDTO(BasePydanticModel):
    """One line of a raw (unsaved) sale used only for profit calculation.

    ``characteristics`` (exposed under that JSON key, ``char_values`` in Python)
    are resolved to a ``variant_id`` server-side before inventory allocation.
    """

    entry_id: ID_T
    price: Decimal
    discount: Decimal = Decimal("0")
    count: Decimal = Field(gt=Decimal("0"))
    expires_at: Optional[date] = None
    char_values: List[CharValueDTO] = Field(
        default_factory=list,
        alias="characteristics",
        max_length=item_constraints.CHAR_VALUES_MAX_COUNT,
    )


class SaleProfitDocumentDTO(BasePydanticModel):
    """The minimal raw sale payload needed to compute profit: where the goods
    leave from (``credit_id`` — the storage), the currency/rate to express
    revenue in base currency, and the sold lines."""

    credit_id: ID_T
    currency_id: ID_T
    rate: ATRate
    items: List[SaleProfitDocumentItemDTO] = Field(
        min_length=1,
        max_length=doc_constraints.ITEM_MAX_COUNT,
    )


class SaleProfitQuery(Query):
    """Compute the profit of a sale. Exactly one source must be given:

    - ``document`` — a raw, unsaved sale; allocate its lines against current
      stock and return the projected profit (error if remains insufficient).
    - ``document_id`` — an existing sale; for a pending doc this projects the
      profit like ``document``, for a confirmed doc it returns the realized
      profit derived from the consumption ledger.
    """

    document: Optional[SaleProfitDocumentDTO] = None
    document_id: Optional[ID_T] = None

    @model_validator(mode="before")
    @classmethod
    def _exactly_one_source(cls, data):
        if isinstance(data, dict):
            has_document = data.get("document") is not None
            has_document_id = data.get("document_id") is not None

            if has_document == has_document_id:
                raise ValueError("Provide exactly one of 'document' or 'document_id'.")

        return data


class SaleDocumentItemsProfitQuery(ListQuery, OrderingQueryMixin, metaclass=FilterMeta):
    _ordering_allowed_fields: OrderingAllowedFieldsT = {
        "created_at",
    }
