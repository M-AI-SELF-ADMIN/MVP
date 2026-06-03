# MVP

Minimal Python project scaffold with a working test setup and a tiny
architecture-aligned core for eventing + memory.

## Quick start
# Persistent Adaptive Engineering Process (PAEP)

A minimal Python project scaffold with a clean `src/` layout, testing, linting, and type checking.

## Installation

Choose one of the following approaches.

### Option A: Development install (recommended)

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
pip install -U pip
pip install -e .[dev]
```

### Option B: If extras are not configured yet

```bash
python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -e .
pip install pytest ruff mypy
```

## Quick usage examples

### Import and call from Python

```python
from mvp import add

print(add(1, 2))   # 3
print(add(-5, 8))  # 3
print(add(0, 0))   # 0
```

### Try in a one-liner

```bash
python -c "from mvp import add; print(add(10, 32))"
```

### Run tests

```bash
pytest
```

## Development workflow

Use this sequence before opening a PR.

1. **Format and lint**
   ```bash
   ruff format .
   ruff check .
   ```
2. **Type check**
   ```bash
   mypy src
   ```
3. **Run test suite**
   ```bash
   pytest
   ```

If your environment requires explicit module resolution, use:

```bash
PYTHONPATH=src pytest
A seed repository for building reflective, adaptive, memory-native engineering runtimes.

## Features

- Persistent memory layer
- Adaptive orchestration runtime
- Reflection engine
- Mutation/evolution pipeline
- Governance and coherence validation
- Regeneration checkpoints

## Quick Start

```bash
python runtime/main.py
```

## Architecture

```
intent -> execution -> observation -> memory
       -> reflection -> mutation -> validation
       -> evolution -> persistence
```

## Project goals

- Keep a small, readable baseline Python package template.
- Provide a fast feedback loop for tests, linting, and typing.
- Stay easy to extend into real application or library code.

## Roadmap milestones

- **Milestone 1: Foundation (current)**
  - Stable package layout and import path.
  - Passing tests for core functions.
- **Milestone 2: Developer tooling hardening**
  - Ensure `.[dev]` extras are fully defined and reproducible.
  - Add CI to enforce lint/test/typecheck on every change.
- **Milestone 3: API growth and documentation**
  - Expand public API beyond arithmetic demo helpers.
  - Add `docs/` with MkDocs or Sphinx once API surface grows.
- **Milestone 4: Distribution readiness**
  - Versioning/release process.
  - Packaging and publishing checks.
