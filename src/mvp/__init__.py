"""Top-level public API for the :mod:`mvp` package."""

from .math_ops import add

from mvp.core import Event, EventBus
from mvp.memory import MemoryRecord, VectorMemory


def add(a: int, b: int) -> int:
    return a + b


__all__ = [
    "Event",
    "EventBus",
    "MemoryRecord",
    "VectorMemory",
    "add",
]
"""Public API surface for the MVP package."""

from .math_ops import add

__all__ = ["add"]
