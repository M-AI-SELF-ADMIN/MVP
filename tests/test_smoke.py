"""Smoke tests for the package public API."""

import mvp
from mvp import Event, EventBus, MemoryRecord, VectorMemory, add

EXPECTED_PUBLIC_API = [
    "Event",
    "EventBus",
    "MemoryRecord",
    "VectorMemory",
    "add",
]


def test_add_smoke() -> None:
    assert add(1, 2) == 3


def test_public_api_exports_are_explicit_and_stable() -> None:
    assert mvp.__all__ == EXPECTED_PUBLIC_API


def test_public_api_names_are_importable_from_package_root() -> None:
    assert Event is mvp.Event
    assert EventBus is mvp.EventBus
    assert MemoryRecord is mvp.MemoryRecord
    assert VectorMemory is mvp.VectorMemory
    assert add is mvp.add


def test_public_api_implementation_can_live_in_domain_modules() -> None:
    assert add.__module__ == "mvp.math_ops"
    assert Event.__module__ == "mvp.core"
    assert EventBus.__module__ == "mvp.core"
    assert MemoryRecord.__module__ == "mvp.memory"
    assert VectorMemory.__module__ == "mvp.memory"


def test_star_import_matches_declared_public_api() -> None:
    namespace: dict[str, object] = {}
    exec("from mvp import *", {}, namespace)

    assert sorted(namespace) == sorted(EXPECTED_PUBLIC_API)


def test_public_api_has_no_extra_domain_module_exports() -> None:
    public_names = sorted(name for name in dir(mvp) if not name.startswith("_"))

    assert public_names == EXPECTED_PUBLIC_API
