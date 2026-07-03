from anbor_types import BasePydanticModel, Command, ID_T
from anbor_types.warehouse.business_document.return_in.dto import (
    ReturnInBusinessDocumentCreateDTO,
    ReturnInBusinessDocumentUpdateDTO,
)


class ReturnInBusinessDocumentCreateCommand(
    ReturnInBusinessDocumentCreateDTO, Command
): ...


class ReturnInBusinessDocumentUpdateCommand(ReturnInBusinessDocumentUpdateDTO, Command):
    id: ID_T


class ReturnInBusinessDocumentDeleteCommand(BasePydanticModel, Command):
    id: ID_T
