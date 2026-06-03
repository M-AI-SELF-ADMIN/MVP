"""Memory layer primitives inspired by the architecture diagram."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class MemoryRecord:
    key: str
    text: str


class VectorMemory:
    """Minimal key/text memory abstraction.

    This keeps the scaffold lightweight while providing an obvious extension point
    for embedding-backed retrieval.
    """

    def __init__(self) -> None:
        self._records: dict[str, MemoryRecord] = {}

    def upsert(self, key: str, text: str) -> MemoryRecord:
        record = MemoryRecord(key=key, text=text)
        self._records[key] = record
        return record

    def get(self, key: str) -> MemoryRecord | None:
        return self._records.get(key)
