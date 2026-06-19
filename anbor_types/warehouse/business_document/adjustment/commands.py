from anbor_types import Command
from anbor_types.warehouse.business_document.adjustment.dto import (
    AdjustmentDocumentCreateDTO,
)


class AdjustmentDocumentCreateCommand(AdjustmentDocumentCreateDTO, Command): ...
