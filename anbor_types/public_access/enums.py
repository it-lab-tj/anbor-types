from enum import StrEnum


class PublicLinkContentTypeEnum(StrEnum):
    """What a public link points at.

    The values are the legacy Django ``app_label_modelname`` strings and are
    persisted in ``common_publiclink.content_type``, so they cannot be renamed
    without a data migration -- ``storage_stockoperationgroup`` in particular
    names a model that no longer exists (it is today's ``BusinessDocument``).

    ``SERVICE`` has no legacy rows: the old project only ever shared products
    and stock-operation groups.
    """

    PRODUCT = "handbook_product"
    SERVICE = "handbook_service"
    BUSINESS_DOCUMENT = "storage_stockoperationgroup"
