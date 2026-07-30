# Contributing

Thanks for contributing to `mvp`. This guide covers local setup, common quality checks, and expectations for branches and commits.

## Development setup

1. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

   On Windows PowerShell, activate with `.venv\\Scripts\\Activate.ps1`.

2. Upgrade packaging tools and install the project in editable mode:

   ```bash
   python -m pip install --upgrade pip
   python -m pip install -e .
   ```

3. Install development tools from the dependency group when your package manager supports PEP 735 dependency groups:

   ```bash
   python -m pip install --group dev
   ```

   If your local `pip` version does not support dependency groups yet, install the tools listed in `pyproject.toml` manually.

## Common commands

Use the `Makefile` targets when possible:

- `make test` runs the test suite.
- `make lint` runs Ruff lint checks.
- `make typecheck` runs mypy.
- `make format` formats Python files with Ruff.
- `make coverage` runs tests with coverage reporting.
- `make check` runs linting, type checking, and tests.

Equivalent direct commands:

```bash
python -m pytest
ruff check .
mypy src tests
ruff format .
coverage run -m pytest && coverage report
```

## Branch guidance

- Branch from `main` with a short, descriptive name, such as `chore/update-tooling`.
- Keep each branch focused on one logical change.
- Rebase or merge the latest `main` before opening a pull request when practical.

## Commit guidance

- Keep commits small and logically grouped.
- Use imperative commit messages, for example `Add coverage configuration`.
- Run `make check` before pushing or opening a pull request.
