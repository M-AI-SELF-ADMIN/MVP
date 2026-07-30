# MVP

MVP is a minimal Python project scaffold for building reflective, adaptive,
memory-native engineering runtimes. It combines a clean `src/` package layout
with a tiny public API for arithmetic smoke tests, event publishing/replay, and
in-memory record storage.

## Package surface

- `mvp.add(a, b)` returns the sum of two integers and acts as a simple import
  sanity check.
- `mvp.core.Event` and `mvp.core.EventBus` provide an in-memory event stream
  that can be published to and replayed by topic.
- `mvp.memory.MemoryRecord` and `mvp.memory.VectorMemory` provide a small
  key/text memory seam that can later grow into embedding-backed retrieval.

## Installation

Use an isolated virtual environment, then install the package in editable mode
with development dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e .[dev]
```

On Windows PowerShell, activate the environment with:

```powershell
.venv\Scripts\Activate.ps1
```

If development extras are unavailable in your packaging toolchain, install the
package and tools explicitly instead:

```bash
python -m pip install -e .
python -m pip install pytest ruff mypy build
```

## Quick usage examples

### Add numbers from Python

```python
from mvp import add

print(add(10, 32))
print(add(-5, 8))
```

### Publish and replay events

```python
from mvp.core import Event, EventBus

bus = EventBus()
bus.publish(Event(topic="intent.received", payload={"goal": "draft roadmap"}))
bus.publish(Event(topic="memory.updated", payload={"key": "roadmap:v1"}))

all_events = bus.replay()
memory_events = bus.replay("memory.updated")

print(len(all_events))      # 2
print(memory_events[0].payload["key"])  # roadmap:v1
```

### Store and retrieve memory records

```python
from mvp.memory import VectorMemory

memory = VectorMemory()
memory.upsert("roadmap:v1", "Ship a stable scaffold, then grow the API.")

record = memory.get("roadmap:v1")
if record is not None:
    print(record.text)
```

### Run the demo runtime

```bash
python runtime/main.py
```

## Development workflow

Install the development environment first:

```bash
python -m pip install -e .[dev]
```

Before opening a pull request, run the same quality gates locally:

```bash
ruff format .
ruff check .
mypy src tests
pytest
```

Common shortcuts are available through `make`:

```bash
make format
make lint
make typecheck
make test
make check
```

## Project goals

- Keep the repository small, readable, and easy to install for new contributors.
- Provide a working Python package baseline with tests, linting, and type
  checking.
- Preserve a clear seam between runtime orchestration, eventing, and memory.
- Grow toward a reflective engineering runtime without hiding the core concepts
  behind heavy infrastructure.

## Roadmap milestones

1. **Foundation:** maintain the package skeleton, importable public API, smoke
   tests, and release notes.
2. **Quality gates:** stabilize Ruff, mypy, pytest, and coverage configuration;
   enforce the workflow in CI.
3. **Runtime coherence:** connect event flow, memory updates, reflection, and
   governance checks into a documented local loop.
4. **API growth:** expand event and memory abstractions with usage-focused tests
   and backwards-compatible public interfaces.
5. **Documentation expansion:** grow the existing `docs/` folder with API guides,
   architecture notes, and contributor workflows. If the API becomes large
   enough, adopt MkDocs or Sphinx for versioned, navigable documentation.

## Architecture

```text
intent -> execution -> observation -> memory
       -> reflection -> mutation -> validation
       -> evolution -> persistence
```

The current codebase keeps this architecture intentionally lightweight:

- `EventBus` approximates the event-bus path for local experiments.
- `VectorMemory` provides a starter seam for future embedding-backed retrieval.
- Runtime modules under `runtime/` sketch reflection, mutation, and persistence
  concepts that can be hardened as the project matures.

## Versioning and changelog

This project follows [Semantic Versioning](https://semver.org/):

- **MAJOR** versions contain incompatible API changes.
- **MINOR** versions add backwards-compatible functionality.
- **PATCH** versions contain backwards-compatible bug fixes.

Released and unreleased changes are tracked in [`CHANGELOG.md`](./CHANGELOG.md)
using the Keep a Changelog structure.

## Release process

1. Update `CHANGELOG.md` under `Unreleased`.
2. Bump `project.version` in `pyproject.toml`.
3. Move release notes from `Unreleased` to a dated version section.
4. Commit and push.
5. Create and push a SemVer tag, such as `v0.2.0`.
