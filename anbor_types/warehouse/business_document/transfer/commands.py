from anbor_types import Command
from anbor_types.warehouse.business_document.transfer.dto import (
    TransferDocumentCreateDTO,
)
from anbor_types.warehouse.business_document_item.commands import (
    BusinessDocumentItemCreateCommand,
)


class TransferDocumentCreateCommand(
    TransferDocumentCreateDTO[BusinessDocumentItemCreateCommand], Command
): ...
