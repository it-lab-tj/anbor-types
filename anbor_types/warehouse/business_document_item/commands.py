from typing import List

from pydantic import Field

from anbor_types.catalog.category.dto import CharValuePairDTO
from anbor_types.warehouse.business_document_item.dto import (
    BusinessDocumentItemBaseCreateDTO,
)
from anbor_types.warehouse.constants.constraints import (
    document_item as item_constraints,
)


class BusinessDocumentItemCreateCommand(BusinessDocumentItemBaseCreateDTO):
    char_values: List[CharValuePairDTO] = Field(
        default_factory=list,
        max_length=item_constraints.CHAR_VALUES_MAX_COUNT,
    )
