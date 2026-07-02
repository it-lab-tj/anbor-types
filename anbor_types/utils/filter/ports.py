from typing import Protocol, runtime_checkable, Tuple

from anbor_types.utils.filter.types import FilterContainerCollection


@runtime_checkable
class FilterCompilerProto[TReturn](Protocol):
    """Compiler for parsed set of FilterSpecs"""

    def compile(self, containers: FilterContainerCollection) -> Tuple[TReturn, ...]:
        """Compiles filter field specs for specific tasks"""
