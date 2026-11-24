from datetime import datetime
from typing import Optional

import msgspec

from anbor_types import INT_ID_T
from anbor_types.identity.user.dto import AuthorInfoShortDTO


class DbSyncHistoryDTO(msgspec.Struct):
    id: INT_ID_T
    # The table kept bigint ids (excluded from the UUIDv7 migration as a log
    # table). The path is relative to the backup storage root.
    backup_path: Optional[str]
    success: bool
    created_at: datetime
    finished_at: Optional[datetime]
    created_by: AuthorInfoShortDTO
