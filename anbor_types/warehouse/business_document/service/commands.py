from anbor_types.warehouse.business_document_item.dto import (
    BusinessDocumentItemUpdateDTO,
)
from anbor_types import ID_T, BasePydanticModel, Command
from anbor_types.warehouse.business_document.service.dto import (
    ServiceDocumentCreateDTO,
    ServiceDocumentUpdateDTO,
)
from anbor_types.warehouse.business_document_item.commands import (
    BusinessDocumentItemCreateCommand,
)


class ServiceDocumentCreateCommand(
    ServiceDocumentCreateDTO[BusinessDocumentItemCreateCommand], Command
): ...


class ServiceDocumentUpdateBodyDTO(
    ServiceDocumentUpdateDTO[BusinessDocumentItemUpdateDTO]
):
    """The PUT body: the generic bound to this action's item type.

    Named rather than left as an inline parameterisation so the OpenAPI
    schema reads ``ServiceDocumentUpdateBodyDTO`` instead of
    ``ServiceDocumentUpdateDTO_BusinessDocumentItemUpdateDTO_``. The create side gets clean
    names the same way, through its concrete command classes.
    """


class ServiceDocumentUpdateCommand(ServiceDocumentUpdateBodyDTO, Command):
    id: ID_T


class ServiceDocumentDeleteCommand(BasePydanticModel, Command):
    id: ID_T
