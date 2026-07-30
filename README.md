# MVP

A minimal Python project scaffold with a clean `src/` layout, testing, linting, type checking, and validated package distribution.

## Package surface

- `mvp.add(a, b)` simple sanity function.
- `mvp.core.Event` / `mvp.core.EventBus` for in-memory event publish and replay.
- `mvp.memory.MemoryRecord` / `mvp.memory.VectorMemory` for minimal memory upsert/get.

## Installation

Use an isolated virtual environment, then install the package with development dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

If your shell does not support `source`, use the platform equivalent, such as `.venv\\Scripts\\Activate.ps1` on Windows PowerShell.

## Quick usage

```python
from mvp import add

print(add(1, 2))
```

## Development workflow

Run checks locally before opening a PR:

```bash
ruff check .
mypy
pytest --cov=mvp --cov-report=term-missing
python -m build
twine check dist/*
```

CI runs the same quality gates and validates the source distribution and wheel with `python -m build` plus `twine check`.

## Versioning and changelog

This project follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html):

- **MAJOR**: incompatible API changes.
- **MINOR**: backwards-compatible functionality.
- **PATCH**: backwards-compatible bug fixes.

All released and unreleased changes are tracked in [`CHANGELOG.md`](./CHANGELOG.md) using the [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) structure.

## Release process

1. Add user-facing changes under `## [Unreleased]` in `CHANGELOG.md`.
2. Choose the next SemVer version.
3. Update `project.version` in `pyproject.toml`.
4. Move changelog entries from `Unreleased` into a new dated version section.
5. Commit the release changes.
6. Create and push an annotated SemVer tag, for example `git tag -a v0.2.0 -m "Release v0.2.0"`.

Tag pushes matching `v*.*.*` run the publish workflow. The workflow always builds and validates the distribution, verifies the tag matches `pyproject.toml`, and only publishes when the matching repository secret is configured:

- `TEST_PYPI_API_TOKEN` enables TestPyPI publishing.
- `PYPI_API_TOKEN` enables PyPI publishing.

The workflow can also be run manually for either TestPyPI or PyPI; manual publishing is still gated by the required secret.

## Project goals

- Keep a minimal, understandable Python package layout.
- Provide a clean baseline for testing and quality tooling.
- Make local onboarding and package release validation fast for contributors.
