"""Smoke tests for the package public API."""

import mvp
from mvp import add


def test_public_api_exports_add() -> None:
    assert mvp.__all__ == ["add"]
    assert mvp.add is add


def test_public_api_function_origin() -> None:
    # Validate the stable public import path (`mvp.add`) while allowing
    # implementation details to live in dedicated module files.
    assert add.__module__ == "mvp.math_ops"
