from anbor_types.warehouse.business_document_item.dto import (
    BusinessDocumentItemUpdateDTO,
)
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


class TransferDocumentUpdateBodyDTO(
    TransferDocumentUpdateDTO[BusinessDocumentItemUpdateDTO]
):
    """The PUT body: the generic bound to this action's item type.

    Named rather than left as an inline parameterisation so the OpenAPI
    schema reads ``TransferDocumentUpdateBodyDTO`` instead of
    ``TransferDocumentUpdateDTO_BusinessDocumentItemUpdateDTO_``. The create side gets clean
    names the same way, through its concrete command classes.
    """


class TransferDocumentUpdateCommand(TransferDocumentUpdateBodyDTO, Command):
    id: ID_T


class TransferDocumentDeleteCommand(BasePydanticModel, Command):
    id: ID_T
