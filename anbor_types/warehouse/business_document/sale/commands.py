from anbor_types import ID_T, BasePydanticModel, Command
from anbor_types.warehouse.business_document.sale.dto import (
    SaleDocumentCreateDTO,
    SaleDocumentUpdateDTO,
)
from anbor_types.warehouse.business_document_item.commands import (
    BusinessDocumentItemCreateCommand,
)


class SaleDocumentCreateCommand(
    SaleDocumentCreateDTO[BusinessDocumentItemCreateCommand], Command
): ...


class SaleDocumentUpdateCommand(SaleDocumentUpdateDTO, Command):
    id: ID_T


class SaleDocumentDeleteCommand(BasePydanticModel, Command):
    id: ID_T
