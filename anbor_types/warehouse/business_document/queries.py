from anbor_types import ListQuery


class BusinessDocumentListQuery(ListQuery):
    """Kind-agnostic listing of all business documents.

    Inherits ``limit``/``offset`` only.

    TODO: filters — subject_id (debit/credit), action, status, date range,
    currency_id, project_id, created_by_id, amount range. The subject filter is
    the key one: it recreates the legacy "counterparty history" view.
    """
