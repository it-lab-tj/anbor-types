from anbor_types import Command
from anbor_types.catalog.service.dto import ServiceCreateDTO, ServiceUpdateDTO
from src.app.shared_kernel.types.base_types import ID_T


class ServiceCreateCommand(ServiceCreateDTO, Command): ...


class ServiceUpdateCommand(ServiceUpdateDTO, Command):
    id: ID_T
