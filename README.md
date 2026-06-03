# MVP

Minimal Python project scaffold with a working test setup and a tiny
architecture-aligned core for eventing + memory.

## Versioning and changelog

This project follows **Semantic Versioning (SemVer)**:

- **MAJOR**: incompatible API changes
- **MINOR**: backwards-compatible functionality
- **PATCH**: backwards-compatible bug fixes

All released and unreleased changes are tracked in [`CHANGELOG.md`](./CHANGELOG.md)
using the Keep a Changelog structure.

## Installation

Use an isolated virtual environment, then install the package in editable mode with development extras:
## Quick start
# Persistent Adaptive Engineering Process (PAEP)

A minimal Python project scaffold with a clean `src/` layout, testing, linting, and type checking.

## Installation

Choose one of the following approaches.

### Option A: Development install (recommended)

```bash
python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -e .[dev]
```

If your shell does not support `source`, use the platform equivalent (for example, `.venv\\Scripts\\activate` on Windows PowerShell).

## Quick usage

### Python REPL

```python
from mvp import add

add(1, 2)      # 3
add(-5, 10)    # 5
add(0, 0)      # 0
```

### One-liner script

```bash
python - <<'PY'
from mvp import add

pairs = [(1, 2), (10, 32), (-3, 7)]
for a, b in pairs:
    print(f"{a} + {b} = {add(a, b)}")
PY
```

## Development workflow

Run checks locally before opening a PR:

```bash
# Lint (if configured in pyproject)
ruff check .

# Type check (if configured in pyproject)
mypy src

# Test suite
pytest
```

If this project is installed with `pip install -e .[dev]`, these tools should be available in your environment.

## Project goals

- Keep a minimal, understandable Python package layout.
- Provide a clean baseline for testing and quality tooling.
- Make local onboarding fast for contributors.

## Roadmap milestones

- **Milestone 1 — Foundation (current):** package skeleton, importable module, and smoke tests.
- **Milestone 2 — Quality gates:** standardize linting and typing config, enforce in CI.
- **Milestone 3 — API growth:** add real library functionality with usage-focused tests.
- **Milestone 4 — Documentation expansion:** add richer API and contributor docs.

## Documentation direction (optional)

When the public API expands, add a `docs/` folder and adopt MkDocs or Sphinx for versioned, navigable documentation.
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
pip install -U pip pytest build
pip install -e .
pytest
python -m build
```

## Release process

1. Update `CHANGELOG.md` under `Unreleased`.
2. Bump `project.version` in `pyproject.toml`.
3. Move release notes from `Unreleased` to a dated version section.
4. Commit and push.
5. Create and push a SemVer tag (for example `v0.2.0`).

Tag pushes matching `v*.*.*` run the publish workflow:

- Publishes to **TestPyPI** if `TEST_PYPI_API_TOKEN` is present.
- Publishes to **PyPI** if `PYPI_API_TOKEN` is present.

You can also run the publish workflow manually and choose `testpypi` or `pypi`.
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
