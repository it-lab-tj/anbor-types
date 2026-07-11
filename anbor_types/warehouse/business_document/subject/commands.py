from anbor_types import ID_T, BasePydanticModel, Command
from anbor_types.warehouse.business_document.subject.dto import (
    SubjectCreateDTO,
    SubjectRebalanceDTO,
    SubjectUpdateDTO,
)


class SubjectCreateCommand(SubjectCreateDTO, Command): ...


class SubjectUpdateCommand(SubjectUpdateDTO, Command):
    id: ID_T


class SubjectDeleteCommand(BasePydanticModel, Command):
    id: ID_T


class SubjectToggleCommand(BasePydanticModel, Command):
    id: ID_T


class SubjectRebalanceCommand(SubjectRebalanceDTO, Command):
    subject_id: ID_T
