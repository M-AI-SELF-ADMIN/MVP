"""Core primitives for the MVP orchestration demo."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class Event:
    """Simple typed event payload used by the event bus."""

    topic: str
    payload: dict[str, Any]


class EventBus:
    """In-memory pub/sub event bus for local testing."""

    def __init__(self) -> None:
        self._events: list[Event] = []

    def publish(self, event: Event) -> None:
        self._events.append(event)

    def replay(self, topic: str | None = None) -> list[Event]:
        if topic is None:
            return list(self._events)
        return [event for event in self._events if event.topic == topic]
