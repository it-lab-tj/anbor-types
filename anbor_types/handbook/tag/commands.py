from anbor_types import ID_T, Command
from anbor_types.handbook.tag.dto import TagCreateDTO, TagUpdateDTO


class TagCreateCommand(TagCreateDTO, Command): ...


class TagToggleStatusCommand(Command):
    id: ID_T


class TagDeleteCommand(Command):
    id: ID_T


class TagUpdateCommand(TagUpdateDTO, Command):
    id: ID_T
