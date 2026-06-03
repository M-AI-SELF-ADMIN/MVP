.PHONY: test lint typecheck format check

test:
	python -m pytest
.PHONY: test lint typecheck format

test:
	pytest

lint:
	ruff check .

typecheck:
	mypy src tests

format:
	ruff format .

check: lint typecheck test
	mypy

format:
	ruff format .
