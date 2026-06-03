# Changelog

All notable changes to this project are documented in this file.
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Established a formal SemVer and changelog process.
- Added build validation in CI with `python -m build`.
- Added optional publishing workflow for PyPI/TestPyPI gated by tags and secrets.
- Initial project scaffolding, tests, packaging metadata, and release workflows.

## [0.1.0] - 2026-05-24

### Added
- Initial project scaffold with package module and smoke test.

---

## Release process

1. Add user-facing changes under `## [Unreleased]` in this file.
2. Choose a new SemVer version:
   - **MAJOR** for incompatible API changes.
   - **MINOR** for backwards-compatible functionality.
   - **PATCH** for backwards-compatible fixes.
3. Update `version` in `pyproject.toml`.
4. Move `Unreleased` entries into a new dated version section.
5. Commit and create an annotated tag, e.g. `v0.2.0`.
6. Push commit and tag.

## Publishing notes

- Tagged releases (for example, `v0.2.0`) trigger the publish workflow.
- Publishing only proceeds when repository secrets are present:
  - `PYPI_API_TOKEN` for production PyPI upload.
  - `TEST_PYPI_API_TOKEN` for TestPyPI upload.
- If no publish secrets are configured, the workflow still runs validation and exits without uploading.
- First tagged release of the MVP package.

[Unreleased]: https://example.com/mvp/compare/v0.1.0...HEAD
[0.1.0]: https://example.com/mvp/releases/tag/v0.1.0
