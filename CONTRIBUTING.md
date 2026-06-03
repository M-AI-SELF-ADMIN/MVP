# Contributing

Thanks for contributing to `mvp`.

## Development setup

1. Create and activate a virtual environment.
2. Install project dependencies (including dev tools):
   - `pip install -e .`
   - `pip install -e .[dev]` if extras are used, or install via your dependency-group workflow.

## Common commands

- Run tests: `pytest`
- Run linting: `ruff check .`
- Run formatting: `ruff format .`
- Run type checks: `mypy`
- Run coverage: `coverage run -m pytest && coverage report`

Or use Make targets:

- `make test`
- `make lint`
- `make format`
- `make typecheck`

## Branch and commit guidance

- Branch from `main` with a descriptive name, for example `feat/add-ci-config`.
- Keep commits focused and logically grouped.
- Write commit messages in imperative mood, e.g. `Add mypy strict configuration`.
- Before opening a PR, run tests, linting, type checks, and formatting.
