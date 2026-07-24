from typing import Any, Protocol, runtime_checkable, Tuple

from anbor_types.utils.filter.types import FilterContainerCollection


@runtime_checkable
class FilterCompilerProto[TReturn](Protocol):
    """Compiler for parsed set of FilterSpecs"""

    def compile(
        self, containers: FilterContainerCollection, /, **meta: Any
    ) -> Tuple[TReturn, ...]:
        """Compiles filter field specs for specific tasks.

        `meta` carries optional per-request context (e.g. a subquery, statement
        or loader options) that individual `compile_<field>__<lookup>` methods
        may consume; implementers must keep it optional for backward compatibility.
        """
