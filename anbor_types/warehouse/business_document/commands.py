from anbor_types import Command, ID_T
from anbor_types.warehouse.business_document.dto import BusinessDocumentChangeTagDTO


class BusinessDocumentConfirmCommand(Command):
    business_document_id: ID_T


class BusinessDocumentChangeTagCommand(BusinessDocumentChangeTagDTO, Command):
    document_id: ID_T
