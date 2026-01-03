from anbor_types import Command
from anbor_types.catalog.product.dto import ProductCreateDTO


class ProductCreateCommand(ProductCreateDTO, Command): ...
