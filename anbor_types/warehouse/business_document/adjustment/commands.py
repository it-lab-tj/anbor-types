from typing import List

from pydantic import Field

from anbor_types import BasePydanticModel, Command, ID_T
from anbor_types.catalog.category.dto import CharValueDTO
from anbor_types.warehouse.business_document.adjustment.dto import (
    AdjustmentDocumentItemUpdateDTO,
    AdjustmentDocumentCreateDTO,
    AdjustmentDocumentItemBaseCreateDTO,
    AdjustmentDocumentUpdateDTO,
)
from anbor_types.warehouse.constants.constraints import (
    document_item as item_constraints,
)


class AdjustmentDocumentItemCreateCommand(AdjustmentDocumentItemBaseCreateDTO):
    char_values: List[CharValueDTO] = Field(
        default_factory=list,
        max_length=item_constraints.CHAR_VALUES_MAX_COUNT,
    )


class AdjustmentDocumentCreateCommand(
    AdjustmentDocumentCreateDTO[AdjustmentDocumentItemCreateCommand], Command
): ...


class AdjustmentDocumentUpdateBodyDTO(
    AdjustmentDocumentUpdateDTO[AdjustmentDocumentItemUpdateDTO]
):
    """The PUT body: the generic bound to this action's item type.

    Named rather than left as an inline parameterisation so the OpenAPI
    schema reads ``AdjustmentDocumentUpdateBodyDTO`` instead of
    ``AdjustmentDocumentUpdateDTO_AdjustmentDocumentItemUpdateDTO_``. The create side gets clean
    names the same way, through its concrete command classes.
    """


class AdjustmentDocumentUpdateCommand(AdjustmentDocumentUpdateBodyDTO, Command):
    id: ID_T


class AdjustmentDocumentDeleteCommand(BasePydanticModel, Command):
    id: ID_T
