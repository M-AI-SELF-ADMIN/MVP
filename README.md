# MVP

Minimal Python project scaffold with a working test setup.

## Versioning and changelog

This project follows **Semantic Versioning (SemVer)**:

- **MAJOR**: incompatible API changes
- **MINOR**: backwards-compatible functionality
- **PATCH**: backwards-compatible bug fixes

All released and unreleased changes are tracked in [`CHANGELOG.md`](./CHANGELOG.md)
using the Keep a Changelog structure.

## Quick start

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
