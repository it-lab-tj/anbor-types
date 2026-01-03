import msgspec

from anbor_types import ID_T


class ModuleConnectResult(msgspec.Struct):
    """Result after company module connection"""

    id: ID_T
