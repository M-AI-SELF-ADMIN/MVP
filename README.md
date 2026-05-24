# MVP

Minimal Python project scaffold with a working test setup.

## Installation

Use an isolated virtual environment, then install the package in editable mode with development extras:

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
