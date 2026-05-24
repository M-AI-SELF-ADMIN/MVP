.PHONY: test lint typecheck format check

test:
	python -m pytest

lint:
	ruff check .

typecheck:
	mypy src tests

format:
	ruff format .

check: lint typecheck test
