.PHONY: test lint typecheck format coverage check build

test:
	python -m pytest

lint:
	ruff check .

typecheck:
	mypy src tests

format:
	ruff format .

coverage:
	coverage run -m pytest
	coverage report

check: lint typecheck test

build:
	python -m build
