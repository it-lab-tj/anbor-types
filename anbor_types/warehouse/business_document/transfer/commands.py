from anbor_types.warehouse.business_document_item.dto import (
    TransferDocumentItemUpdateDTO,
)
from anbor_types import ID_T, BasePydanticModel, Command
from anbor_types.warehouse.business_document.transfer.dto import (
    TransferDocumentCreateDTO,
    TransferDocumentUpdateDTO,
)
from anbor_types.warehouse.business_document_item.commands import (
    TransferDocumentItemCreateCommand,
)


class TransferDocumentCreateCommand(
    TransferDocumentCreateDTO[TransferDocumentItemCreateCommand], Command
): ...


class TransferDocumentUpdateBodyDTO(
    TransferDocumentUpdateDTO[TransferDocumentItemUpdateDTO]
):
    """The PUT body: the generic bound to this action's item type.

    Named rather than left as an inline parameterisation so the OpenAPI
    schema reads ``TransferDocumentUpdateBodyDTO`` instead of
    ``TransferDocumentUpdateDTO_TransferDocumentItemUpdateDTO_``. The create side gets clean
    names the same way, through its concrete command classes.
    """


class TransferDocumentUpdateCommand(TransferDocumentUpdateBodyDTO, Command):
    id: ID_T


class TransferDocumentDeleteCommand(BasePydanticModel, Command):
    id: ID_T
