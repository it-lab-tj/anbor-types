from anbor_types import Command
from anbor_types.warehouse.business_document.sale.dto import SaleDocumentCreateDTO
from anbor_types.warehouse.business_document_item.commands import (
    BusinessDocumentItemCreateCommand,
)


class SaleDocumentCreateCommand(
    SaleDocumentCreateDTO[BusinessDocumentItemCreateCommand], Command
): ...
