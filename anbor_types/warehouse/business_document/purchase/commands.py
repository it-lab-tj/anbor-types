from anbor_types.warehouse.business_document.purchase.dto import (
    PurchaseDocumentCreateDTO,
)

from anbor_types import Command
from anbor_types.warehouse.business_document_item.commands import (
    BusinessDocumentItemCreateCommand,
)


class PurchaseDocumentCreateCommand(
    PurchaseDocumentCreateDTO[BusinessDocumentItemCreateCommand], Command
): ...
