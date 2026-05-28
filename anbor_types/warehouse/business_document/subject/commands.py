from anbor_types import Command
from anbor_types.warehouse.business_document.subject.dto import SubjectCreateDTO


class SubjectCreateCommand(SubjectCreateDTO, Command): ...
