# Contributing

Thanks for contributing to this project.

## Development setup

1. Create and activate a virtual environment:
   - `python -m venv .venv`
   - `source .venv/bin/activate`
2. Upgrade packaging tools:
   - `python -m pip install --upgrade pip`
3. Install development dependencies:
   - `python -m pip install -e .`
   - `python -m pip install pytest ruff mypy coverage build twine`

## Common commands

- Run tests: `make test`
- Run lint checks: `make lint`
- Run type checking: `make typecheck`
- Auto-format code: `make format`

You can also run all checks with `make check`.

## Branch and commit guidance

- Create a focused branch per change, for example: `feat/add-coverage-config` or `chore/update-tooling`.
- Keep commits small and meaningful.
- Use clear commit messages in the imperative mood, for example:
  - `Add mypy configuration`
  - `Add dev dependency group`
- Before opening a PR, run `make check` and ensure all commands pass.
