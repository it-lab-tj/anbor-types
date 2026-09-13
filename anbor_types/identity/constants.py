from enum import IntEnum, StrEnum


class OtpKindEnum(IntEnum):
    """What a one-time code is *for*.

    Values are append-only — they are persisted in ``accounts_otp.kind`` and
    pinned by a CHECK constraint, so renumbering would silently reinterpret
    existing rows.
    """

    EMAIL_CONFIRMATION = 1
    PHONE_CONFIRMATION = 2
    FORGOT_PASSWORD = 3
    INVITATION = 4


class PermissionBoundaryEnum(StrEnum):
    """The area of the product a permission applies to.

    A boundary is deliberately independent of any table or Django content type:
    tables get renamed and models get split, while a permission's identity has
    to stay put. Values are persisted -- in permission codenames
    (``<boundary>.<action>``) and in
    ``identity_jobposition_permittedobject.boundary`` -- so they are
    append-only; renaming a member silently reinterprets stored rows.

    Only boundaries that own addressable objects can be scoped per object
    (currently ``STORAGE`` and ``CASH_DESK``); the rest are all-or-nothing.
    """

    # documents -- one per BusinessDocumentActionEnum
    ADJUSTMENT = "adjustment"
    PURCHASE = "purchase"
    RETURN_IN = "return_in"
    RETURN_OUT = "return_out"
    SALE = "sale"
    SERVICE_SALE = "service_sale"
    TRANSFER = "transfer"

    # subjects -- one per SubjectKindEnum
    CLIENT = "client"
    PERFORMER = "performer"
    STORAGE = "storage"

    # catalog
    CATEGORY = "category"
    MEASUREMENT_UNIT = "measurement_unit"
    PRODUCT = "product"
    SERVICE = "service"

    # money
    CASH_DESK = "cash_desk"
    CURRENCY = "currency"
    EXCHANGE_RATE = "exchange_rate"
    EXPENSE_ORDER = "expense_order"
    INCOME_ORDER = "income_order"
    OPERATING_EXPENSE = "operating_expense"

    # handbook
    COUNTRY = "country"
    GALLERY = "gallery"
    PROJECT = "project"
    REGION = "region"

    # organisation
    COMPANY = "company"
    DISMISSAL_NOTE = "dismissal_note"
    JOB_POSITION = "job_position"
    STAFF = "staff"
    USER = "user"

    # analytics
    REPORT = "report"
    STATISTIC = "statistic"

    # platform
    MODULE = "module"
    OPERATION_HISTORY = "operation_history"
