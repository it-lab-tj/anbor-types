from enum import IntEnum


class DbSyncActionEnum(IntEnum):
    """Persisted in ``internal_dbsynchistory.action``; values come from the legacy model."""

    BACKUP = 1
    RESTORE = 2


class DbSyncDbTypeEnum(IntEnum):
    PGSQL = 1
