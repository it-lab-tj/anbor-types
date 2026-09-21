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

    Only boundaries that own addressable objects can be scoped per object --
    the subjects (``STORAGE``, ``CLIENT``, ``PERFORMER``) and ``CASH_DESK``;
    the rest are all-or-nothing.
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

    # analytics -- reports and dashboards are route-based, so they are one
    # boundary with a permission per route rather than two that would split on
    # nothing.
    STATISTIC = "statistic"

    # platform
    MODULE = "module"

    # money, continued -- the third wallet document kind, beside INCOME_ORDER
    # and EXPENSE_ORDER. Appended here rather than next to them because id
    # windows are handed out in declaration order: a member inserted mid-list
    # would shift every boundary after it onto other rows' ids.
    TRANSFER_ORDER = "transfer_order"


class PermissionActionEnum(StrEnum):
    """What a permission lets you do within its boundary.

    The other half of a codename (``<boundary>.<action>``), and persisted in the
    same two places, so members are append-only for the same reason
    ``PermissionBoundaryEnum``'s are.

    Actions are deliberately not pure CRUD. The permissions this vocabulary
    replaces were written as bundles -- "create, edit, deactivate and delete" is
    one checkbox to the people granting it -- so ``MANAGE`` is a first-class
    action rather than three the UI would always tick together. The scoped
    ``READ_*`` members exist for the same reason: "see the balance" and "see the
    sale history" are separately grantable in a way a single ``READ`` could not
    express.
    """

    # lifecycle
    READ = "read"
    CREATE = "create"
    UPDATE = "update"
    DELETE = "delete"
    # Write access as one checkbox: create + update + delete + activate /
    # deactivate. It does NOT include READ -- every boundary declares its own
    # read, so "may look" is always grantable without "may change". A boundary
    # declares either MANAGE or the separate write actions, never both; the
    # catalog refuses to import otherwise.
    MANAGE = "manage"

    # workflow
    CONFIRM = "confirm"
    IMPORT = "import"
    TUNE = "tune"
    IGNORE_DISCOUNT = "ignore_discount"
    REBALANCE = "rebalance"
    RECALCULATE = "recalculate"
    TRANSFER = "transfer"
    # Narrows a boundary to named objects instead of all of them. A position
    # holding this marker reaches only the objects listed for it in
    # `identity_jobposition_permittedobject`; without the marker it reaches
    # every object of the boundary. Declared for the subjects (`storage`,
    # `client`, `performer`) and `cash_desk`.
    #
    # This is a deliberate collapse of what v1 did. There, a per-object row
    # carried its own bitmask, so a position could hold different rights on
    # different objects -- read one storage, write another. Here the object rows
    # are membership only: the boundary's actions apply, and they apply to every
    # object in the scope. That trades granularity nobody was using for a rule
    # that can be reasoned about, and it is reversible -- per-object rights would
    # come back as rows pairing an object with a permission id, not as a bitmask.
    #
    # How scope is read (the rules live with the capability service):
    #   * a boundary's own objects -- the list, a balance, a history -- are
    #     strict: the object must be in reach for the permission checked;
    #   * a document is visible when ANY scoped object it references is in
    #     reach -- reading is a lens over what the user is assigned to;
    #   * a document is writable only when EVERY scoped object it references
    #     is in reach -- writing acts on each of them.
    ACCESS_SCOPED_OBJECTS = "access_scoped_objects"

    # scoped reads -- each is separately grantable
    READ_ARCHIVE = "read_archive"
    READ_BALANCE = "read_balance"
    READ_NEGATIVE_BALANCE = "read_negative_balance"
    READ_POSITIVE_BALANCE = "read_positive_balance"
    READ_PAYMENTS = "read_payments"
    READ_STOCK = "read_stock"
    READ_PURCHASE_PRICE = "read_purchase_price"
    READ_MARGIN = "read_margin"
    READ_MIN_PRICE = "read_min_price"
    READ_MAX_DISCOUNT = "read_max_discount"
    READ_PROFIT = "read_profit"
    READ_PROFIT_PREVIEW = "read_profit_preview"

    # scoped history reads
    READ_HISTORY = "read_history"
    READ_ADJUSTMENT_HISTORY = "read_adjustment_history"
    READ_EXPENSE_HISTORY = "read_expense_history"
    READ_INCOME_HISTORY = "read_income_history"
    READ_PURCHASE_HISTORY = "read_purchase_history"
    READ_SALE_HISTORY = "read_sale_history"
    READ_SERVICE_SALE_HISTORY = "read_service_sale_history"
    READ_TRANSFER_HISTORY = "read_transfer_history"
    READ_RETURN_IN_HISTORY = "read_return_in_history"
    READ_RETURN_OUT_HISTORY = "read_return_out_history"
    READ_RECALCULATE_HISTORY = "read_recalculate_history"

    # analytics reads -- one per report or dashboard panel
    READ_PROFIT_LOSS = "read_profit_loss"
    READ_INCOME_STATEMENT = "read_income_statement"
    READ_WALLET_CASH_FLOW = "read_wallet_cash_flow"
    READ_COMPANY_SUMMARY = "read_company_summary"
    READ_DAILY = "read_daily"
    READ_LIQUID_INVENTORY = "read_liquid_inventory"
    READ_ILLIQUID_INVENTORY = "read_illiquid_inventory"
    READ_PURCHASE_SUGGESTIONS = "read_purchase_suggestions"
    READ_WAREHOUSE_OVERVIEW = "read_warehouse_overview"
    READ_WAREHOUSE_CASH_FLOW = "read_warehouse_cash_flow"
    READ_WAREHOUSE_CATEGORY_FLOW = "read_warehouse_category_flow"
