from typing import List

from pydantic import Field
from anbor_types.warehouse.constants.constraints import (
    document_item as item_constraints,
)

from anbor_types import ID_T, BasePydanticModel, Command
from anbor_types.catalog.category.dto import CharValueDTO
from anbor_types.warehouse.business_document.sale.dto import (
    SaleDocumentCreateDTO,
    SaleDocumentUpdateDTO,
)
from anbor_types.warehouse.business_document_item.dto import (
    BusinessDocumentItemBaseCreateDTO,
)


class SaleDocumentItemCreateCommand(BusinessDocumentItemBaseCreateDTO):
    char_values: List[CharValueDTO] = Field(
        default_factory=list,
        max_length=item_constraints.CHAR_VALUES_MAX_COUNT,
    )


class SaleDocumentCreateCommand(
    SaleDocumentCreateDTO[SaleDocumentItemCreateCommand], Command
): ...


class SaleDocumentUpdateCommand(SaleDocumentUpdateDTO, Command):
    id: ID_T


class SaleDocumentDeleteCommand(BasePydanticModel, Command):
    id: ID_T
