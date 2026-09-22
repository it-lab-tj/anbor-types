from typing import List

from pydantic import Field
from anbor_types.warehouse.constants.constraints import (
    document_item as item_constraints,
)

from anbor_types.warehouse.business_document_item.dto import (
    BusinessDocumentItemUpdateDTO,
)
from anbor_types import ID_T, BasePydanticModel, Command
from anbor_types.catalog.category.dto import CharValueDTO
from anbor_types.warehouse.business_document.sale.dto import (
    SaleDocumentCreateDTO,
    SaleDocumentUpdateDTO,
)
from anbor_types.warehouse.business_document_item.dto import (
    BusinessDocumentItemCreateDTO,
)


class SaleDocumentItemCreateCommand(BusinessDocumentItemCreateDTO):
    char_values: List[CharValueDTO] = Field(
        default_factory=list,
        max_length=item_constraints.CHAR_VALUES_MAX_COUNT,
    )


class SaleDocumentCreateCommand(
    SaleDocumentCreateDTO[SaleDocumentItemCreateCommand], Command
): ...


class SaleDocumentUpdateBodyDTO(SaleDocumentUpdateDTO[BusinessDocumentItemUpdateDTO]):
    """The PUT body: the generic bound to this action's item type.

    Named rather than left as an inline parameterisation so the OpenAPI
    schema reads ``SaleDocumentUpdateBodyDTO`` instead of
    ``SaleDocumentUpdateDTO_BusinessDocumentItemUpdateDTO_``. The create side gets clean
    names the same way, through its concrete command classes.
    """


class SaleDocumentUpdateCommand(SaleDocumentUpdateBodyDTO, Command):
    id: ID_T


class SaleDocumentDeleteCommand(BasePydanticModel, Command):
    id: ID_T
