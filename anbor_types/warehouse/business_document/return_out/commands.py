from anbor_types import Command

from anbor_types.warehouse.business_document.return_out.dto import (
    ReturnOutBusinessDocumentCreateDTO,
)


class ReturnOutBusinessDocumentCreateCommand(
    ReturnOutBusinessDocumentCreateDTO, Command
): ...
