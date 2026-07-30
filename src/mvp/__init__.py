"""Public API surface for the MVP package."""

from .math_ops import add

__all__ = ["add"]


def __dir__() -> list[str]:
    """Return the stable public package attributes."""
    return ["add", "math_ops"]
