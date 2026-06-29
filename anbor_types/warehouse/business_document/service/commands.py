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


class ServiceDocumentUpdateCommand(ServiceDocumentUpdateDTO, Command):
    id: ID_T


class ServiceDocumentDeleteCommand(BasePydanticModel, Command):
    id: ID_T
