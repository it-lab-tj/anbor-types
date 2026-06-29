from anbor_types.warehouse.business_document.purchase.dto import (
    PurchaseDocumentCreateDTO,
    PurchaseDocumentUpdateDTO,
)

from anbor_types import ID_T, BasePydanticModel, Command
from anbor_types.warehouse.business_document_item.commands import (
    BusinessDocumentItemCreateCommand,
)


class PurchaseDocumentCreateCommand(
    PurchaseDocumentCreateDTO[BusinessDocumentItemCreateCommand], Command
): ...


class PurchaseDocumentUpdateCommand(PurchaseDocumentUpdateDTO, Command):
    id: ID_T


class PurchaseDocumentDeleteCommand(BasePydanticModel, Command):
    id: ID_T
