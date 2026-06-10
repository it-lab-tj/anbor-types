from anbor_types import ID_T, Command
from anbor_types.catalog.service.dto import ServiceCreateDTO, ServiceUpdateDTO


class ServiceCreateCommand(ServiceCreateDTO, Command): ...


class ServiceUpdateCommand(ServiceUpdateDTO, Command):
    id: ID_T
