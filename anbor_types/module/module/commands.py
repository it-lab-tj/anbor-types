from anbor_types import INT_ID_T, Command
from anbor_types.module.module.dto import ModuleConnectDTO


class ModuleConnectCommand(ModuleConnectDTO): ...


class ModuleDeactivateCommand(Command):
    default_module_id: INT_ID_T
