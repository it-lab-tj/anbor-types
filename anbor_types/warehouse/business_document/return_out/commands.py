from anbor_types import BasePydanticModel, Command, ID_T

from anbor_types.warehouse.business_document.return_out.dto import (
    ReturnOutBusinessDocumentCreateDTO,
    ReturnOutBusinessDocumentUpdateDTO,
)


class ReturnOutBusinessDocumentCreateCommand(
    ReturnOutBusinessDocumentCreateDTO, Command
): ...


class ReturnOutBusinessDocumentUpdateCommand(
    ReturnOutBusinessDocumentUpdateDTO, Command
):
    id: ID_T


class ReturnOutBusinessDocumentDeleteCommand(BasePydanticModel, Command):
    id: ID_T
