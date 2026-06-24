from anbor_types import ID_T, BasePydanticModel, Command
from anbor_types.warehouse.business_document.transfer.dto import (
    TransferDocumentCreateDTO,
    TransferDocumentUpdateDTO,
)
from anbor_types.warehouse.business_document_item.commands import (
    BusinessDocumentItemCreateCommand,
)


class TransferDocumentCreateCommand(
    TransferDocumentCreateDTO[BusinessDocumentItemCreateCommand], Command
): ...


class TransferDocumentUpdateCommand(TransferDocumentUpdateDTO, Command):
    id: ID_T


class TransferDocumentDeleteCommand(BasePydanticModel, Command):
    id: ID_T
