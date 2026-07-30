"""Public API smoke tests for the mvp package."""

import mvp
from mvp import *  # noqa: F403


def test_add_smoke() -> None:
    assert mvp.add(1, 2) == 3


def test_public_api_is_explicit_and_stable() -> None:
    assert mvp.__all__ == ["add"]


def test_star_import_tracks_public_api() -> None:
    # ``add`` comes from ``from mvp import *`` and should remain part of the
    # public top-level API contract.
    assert add(2, 3) == 5  # noqa: F405
"""Smoke tests for the package public API."""

import mvp
from mvp import add


def test_add_smoke() -> None:
    assert add(1, 2) == 3


def test_public_api_exports_are_explicit_and_stable() -> None:
    assert mvp.__all__ == ["add"]
    assert sorted(name for name in dir(mvp) if not name.startswith("_")) == ["add", "math_ops"]


def test_public_api_function_origin() -> None:
    # Validate the stable public import path (`mvp.add`) while allowing
    # implementation details to live in dedicated module files.
    assert add is mvp.add
    assert add.__module__ == "mvp.math_ops"
