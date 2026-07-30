# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Documented the SemVer versioning strategy and changelog release process.
- Added CI distribution validation with `python -m build` and `twine check`.
- Added optional PyPI/TestPyPI publishing workflow gated by SemVer tags and repository secrets.

### Fixed

- Normalized `pyproject.toml` package metadata so source and wheel distributions pass validation checks.

## [0.1.0] - 2026-05-24

### Added

- Initial project scaffold with package module and smoke test.

## Release process

1. Add user-facing changes under `## [Unreleased]` in this file.
2. Choose a new SemVer version:
   - **MAJOR** for incompatible API changes.
   - **MINOR** for backwards-compatible functionality.
   - **PATCH** for backwards-compatible fixes.
3. Update `version` in `pyproject.toml`.
4. Move `Unreleased` entries into a new dated version section.
5. Commit and create an annotated tag, e.g. `v0.2.0`.
6. Push the commit and tag.

## Publishing notes

- Tagged releases matching `v*.*.*` trigger the publish workflow.
- The publish workflow verifies the tag version matches `project.version` in `pyproject.toml`.
- Publishing only proceeds when the relevant repository secret is present:
  - `PYPI_API_TOKEN` for production PyPI upload.
  - `TEST_PYPI_API_TOKEN` for TestPyPI upload.
- If no publish secret is configured, validation still runs and upload is skipped.

[Unreleased]: https://github.com/example/mvp/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/example/mvp/releases/tag/v0.1.0
