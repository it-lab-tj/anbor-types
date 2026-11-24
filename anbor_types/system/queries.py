from anbor_types import Query


class DbLastBackupReadQuery(Query):
    """The newest backup started by a user; scheduled runs (no author) are skipped."""
