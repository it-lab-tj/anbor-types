from typing import List

from pydantic import Field

from anbor_types import BasePydanticModel, Command, ID_T
from anbor_types.catalog.category.dto import CharValueDTO
from anbor_types.warehouse.business_document.adjustment.dto import (
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


class AdjustmentDocumentUpdateCommand(AdjustmentDocumentUpdateDTO, Command):
    id: ID_T


class AdjustmentDocumentDeleteCommand(BasePydanticModel, Command):
    id: ID_T
