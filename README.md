# MVP

Minimal Python project scaffold with a working test setup and a tiny
architecture-aligned core for eventing + memory.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -U pip pytest
PYTHONPATH=src pytest
```

## Package surface

- `mvp.add(a, b)` simple sanity function.
- `mvp.Event` / `mvp.EventBus` for in-memory event publish + replay.
- `mvp.MemoryRecord` / `mvp.VectorMemory` for minimal memory upsert/get.

## Why this shape?

This mirrors the diagram at a lightweight level:

- EventBus approximates the ORA event-bus path.
- VectorMemory provides a starter seam for later embedding-backed retrieval.
- Tests validate core behavior so future expansion can happen with confidence.
