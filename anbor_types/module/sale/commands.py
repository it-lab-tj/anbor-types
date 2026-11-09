from decimal import Decimal
from typing import List, Optional

from pydantic import Field

from anbor_types import ID_T, BasePydanticModel, Command
from anbor_types.api.constants import DECIMAL_ZERO
from anbor_types.catalog.category.dto import CharValueDTO
from anbor_types.common.annotated import ATComment, ATDiscount, ATPrice
from anbor_types.warehouse.constants.constraints import document as doc_constraints
from anbor_types.warehouse.constants.constraints import (
    document_item as item_constraints,
)


class MarketplaceSaleItemDTO(BasePydanticModel):
    """One order line, in the feed's terms: ``entry_id`` is the feed item's
    ``id``, ``char_values`` the chosen variant's pairs (empty for a product
    without characteristics)."""

    entry_id: ID_T
    price: ATPrice
    discount: ATDiscount
    count: Decimal = Field(gt=DECIMAL_ZERO, le=item_constraints.COUNT_MAX)
    char_values: List[CharValueDTO] = Field(
        default_factory=list,
        max_length=item_constraints.CHAR_VALUES_MAX_COUNT,
    )


class MarketplaceSaleCreateCommand(BasePydanticModel, Command):
    """An order placed on the marketplace, becoming a PENDING sale.

    Carries no company, storage, client, project or currency: the company is
    whatever the API key resolves to and the rest comes from that company's
    marketplace module, so a caller cannot route a sale anywhere else.
    """

    # Buyer's contact details and note -- the buyer is not a CRM client, the
    # module's single client is, so this is the only place they are kept.
    comment: Optional[ATComment] = None
    items: List[MarketplaceSaleItemDTO] = Field(
        min_length=1,
        max_length=doc_constraints.ITEM_MAX_COUNT,
    )


class MarketplaceSaleConfirmCommand(BasePydanticModel, Command):
    """The marketplace accepted the order: confirm the sale, writing the goods
    off. Idempotent -- a sale a manager already confirmed is left as is."""

    id: ID_T


class MarketplaceSaleRejectCommand(BasePydanticModel, Command):
    """The order was cancelled by the buyer or rejected by a moderator.
    Idempotent, and only for a sale still PENDING."""

    id: ID_T
