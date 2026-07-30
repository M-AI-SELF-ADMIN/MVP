"""Stable public API for the MVP package.

Import application-facing objects from this module instead of reaching into
implementation modules. Domain modules (for example ``mvp.math_ops`` and
``mvp.core``) may evolve independently while the names exported here remain the
supported compatibility surface.
"""

from .core import Event, EventBus
from .math_ops import add
from .memory import MemoryRecord, VectorMemory

__all__ = [
    "Event",
    "EventBus",
    "MemoryRecord",
    "VectorMemory",
    "add",
]


def __dir__() -> list[str]:
    """Return the stable public API for interactive discovery."""
    return sorted(__all__)
