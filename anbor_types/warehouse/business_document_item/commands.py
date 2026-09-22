from typing import List

from pydantic import Field

from anbor_types.catalog.category.dto import CharValueDTO
from anbor_types.warehouse.business_document_item.dto import (
    BusinessDocumentItemCreateDTO,
)
from anbor_types.warehouse.constants.constraints import (
    document_item as item_constraints,
)


class BusinessDocumentItemCreateCommand(BusinessDocumentItemCreateDTO):
    char_values: List[CharValueDTO] = Field(
        default_factory=list,
        max_length=item_constraints.CHAR_VALUES_MAX_COUNT,
    )


# There is no update counterpart: ``char_values`` lives on
# ``BusinessDocumentItemBaseUpdateDTO`` itself, because an update route binds the
# *DTO* (the id comes from the path, not the body) while a create route binds the
# command. A command-only field would be parsed away at the body boundary — which
# is exactly what happened to ``char_values`` on PUT before it moved down.
