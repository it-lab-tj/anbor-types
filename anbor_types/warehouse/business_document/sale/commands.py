from anbor_types import ID_T, Command
from anbor_types.warehouse.business_document.sale.dto import SaleDocumentCreateDTO, SaleDocumentUpdateDTO
from anbor_types.warehouse.business_document_item.commands import (
    BusinessDocumentItemCreateCommand,
    BusinessDocumentItemUpdateCommand,
)


class SaleDocumentCreateCommand(
    SaleDocumentCreateDTO[BusinessDocumentItemCreateCommand], Command
): ...

class SaleDocumentUpdateCommand(
    SaleDocumentUpdateDTO[BusinessDocumentItemUpdateCommand], Command
):
    id: ID_T