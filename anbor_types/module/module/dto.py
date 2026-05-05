from datetime import datetime
from typing import Dict, Optional
import msgspec
from pydantic import Field

from anbor_types import ID_T, BasePydanticModel


class DefaultModuleDTO(msgspec.Struct):
    id: ID_T
    kind: str


class ConnectedModuleListDTO(msgspec.Struct):
    id: ID_T
    kind: str
    created_by_id: ID_T
    updated_at: datetime


class ModuleConnectDTO(BasePydanticModel):
    default_module_id: ID_T
    storage_id: ID_T
    payload: Optional[Dict] = Field(default_factory=dict)


class ModuleConnectListDTO(ModuleConnectDTO):
    id: ID_T


class MarketplaceIntegrationPayloadDTO(BasePydanticModel):
    domain: str
