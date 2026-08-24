from datetime import datetime
from typing import Optional, Union

import msgspec

from anbor_types import ID_T
from anbor_types.catalog.product.dto import ProductDetailedDTO
from anbor_types.catalog.service.dto import ServiceDetailedDTO
from anbor_types.public_access.enums import PublicLinkContentTypeEnum
from anbor_types.warehouse.business_document.adjustment.dto import (
    AdjustmentDocumentDetailedDTO,
)
from anbor_types.warehouse.business_document.purchase.dto import (
    PurchaseDocumentDetailedDTO,
)
from anbor_types.warehouse.business_document.sale.dto import SaleDocumentDetailedDTO
from anbor_types.warehouse.business_document.service.dto import (
    ServiceDocumentDetailedDTO,
)
from anbor_types.warehouse.business_document.transfer.dto import (
    TransferDocumentDetailedDTO,
)


class PublicLinkDTO(msgspec.Struct):
    """A ``common_publiclink`` row, as far as resolving one needs it.

    ``company_id`` is the point of the whole struct: a public request carries no
    user, so the execution context has no company and the link row is the only
    thing that can scope the content lookup.
    """

    id: ID_T
    company_id: ID_T
    content_type: str
    ref_id: str
    is_active: bool
    is_disposal: bool
    available_until: Optional[datetime]


#: What a resolved public link yields. Deliberately the same detailed DTOs the
#: authenticated routes return -- a public link is a view onto the same record,
#: not a separate projection of it.
PublicLinkContentDTO = Union[
    ProductDetailedDTO,
    ServiceDetailedDTO,
    SaleDocumentDetailedDTO,
    PurchaseDocumentDetailedDTO,
    TransferDocumentDetailedDTO,
    AdjustmentDocumentDetailedDTO,
    ServiceDocumentDetailedDTO,
]

__all__ = [
    "PublicLinkContentDTO",
    "PublicLinkContentTypeEnum",
    "PublicLinkDTO",
]
