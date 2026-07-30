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
