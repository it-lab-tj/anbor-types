from anbor_types import Query
from anbor_types.public_access.enums import PublicLinkContentTypeEnum


class PublicLinkReadQuery(Query):
    """Resolve a shared link to the content it points at.

    ``company_nick`` stays in the address even though it identifies nothing on
    its own: ``ref_id`` is a slug or a vendor code depending on the content
    type, and neither is unique across companies -- ``business_document``
    constrains ``vendor_code`` per company, and ``catalog_entry.slug`` is not
    unique at all.
    """

    company_nick: str
    content_type: PublicLinkContentTypeEnum
    ref_id: str
