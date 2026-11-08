from pydantic import Field

from anbor_types import Query
from anbor_types.module.annotated import ATCatalogFeedCursor
from anbor_types.module.constraints import (
    CATALOG_FEED_DEFAULT_LIMIT,
    CATALOG_FEED_INITIAL_CURSOR,
    CATALOG_FEED_MAX_LIMIT,
)


class CatalogFeedQuery(Query):
    """Keyset page, not offset: the cursor is `(change_xid, id)` of the last row
    served, so a row changing between requests cannot shift the page under the
    consumer the way an OFFSET would.
    """

    cursor: ATCatalogFeedCursor = Field(default=CATALOG_FEED_INITIAL_CURSOR)
    limit: int = Field(
        default=CATALOG_FEED_DEFAULT_LIMIT, ge=1, le=CATALOG_FEED_MAX_LIMIT
    )
