from anbor_types import ID_T, Command
from anbor_types.catalog.product.dto import (
    ProductCreateDTO,
    ProductUpdateDTO,
)


class ProductCreateCommand(ProductCreateDTO, Command): ...


class ProductUpdateCommand(ProductUpdateDTO, Command):
    id: ID_T


class ProductDeleteCommand(Command):
    id: ID_T


class ProductToggleCommand(Command):
    id: ID_T
