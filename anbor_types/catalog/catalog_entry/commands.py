from anbor_types import ID_T, Command
from anbor_types.catalog.annotated import ATFileName


class CatalogEntryImportCommand(Command):
    """Entry point of a catalog-entry (product/service) import.

    Carries the uploaded file plus where imported stock should land. The handler
    only persists the file and enqueues the async import job; the worker runs the
    actual pipeline. ``file`` is the raw spreadsheet bytes.
    """

    name: ATFileName
    file: memoryview
    storage_id: ID_T
    project_id: ID_T


class CatalogEntryDeleteCommand(Command):
    id: ID_T
