from anbor_types import Command
from anbor_types.warehouse.business_document.purchase.dto import PurchaseDocumentCreateDTO


class PurchaseDocumentCreateCommand(PurchaseDocumentCreateDTO, Command): ...
