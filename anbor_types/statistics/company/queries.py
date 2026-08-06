from anbor_types import Query


class CompanyAnalyticsSummaryQuery(Query):
    """Ask for the company-wide money totals. Scope comes from the execution
    context, so the query itself carries no parameters."""
