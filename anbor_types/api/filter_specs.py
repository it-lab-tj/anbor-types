from typing import Annotated

from anbor_types.common.enums import StatusEnum
from anbor_types.utils.filter.types import FilterSpec

AFStatus = Annotated[StatusEnum, FilterSpec.enum(StatusEnum)]
