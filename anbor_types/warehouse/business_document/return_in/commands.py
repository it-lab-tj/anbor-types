from anbor_types import Command
from anbor_types.warehouse.business_document.return_in.dto import (
    ReturnInBusinessDocumentCreateDTO,
)


class ReturnInBusinessDocumentCreateCommand(
    ReturnInBusinessDocumentCreateDTO, Command
): ...
