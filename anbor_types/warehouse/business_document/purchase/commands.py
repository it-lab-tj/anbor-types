from anbor_types.warehouse.business_document.purchase.dto import (
    PurchaseDocumentCreateDTO,
    PurchaseDocumentUpdateDTO,
)

from anbor_types.warehouse.business_document_item.dto import (
    BusinessDocumentItemUpdateDTO,
)
from anbor_types import ID_T, BasePydanticModel, Command
from anbor_types.warehouse.business_document_item.commands import (
    BusinessDocumentItemCreateCommand,
)


class PurchaseDocumentCreateCommand(
    PurchaseDocumentCreateDTO[BusinessDocumentItemCreateCommand], Command
): ...


class PurchaseDocumentUpdateBodyDTO(
    PurchaseDocumentUpdateDTO[BusinessDocumentItemUpdateDTO]
):
    """The PUT body: the generic bound to this action's item type.

    Named rather than left as an inline parameterisation so the OpenAPI
    schema reads ``PurchaseDocumentUpdateBodyDTO`` instead of
    ``PurchaseDocumentUpdateDTO_BusinessDocumentItemUpdateDTO_``. The create side gets clean
    names the same way, through its concrete command classes.
    """


class PurchaseDocumentUpdateCommand(PurchaseDocumentUpdateBodyDTO, Command):
    id: ID_T


class PurchaseDocumentDeleteCommand(BasePydanticModel, Command):
    id: ID_T
