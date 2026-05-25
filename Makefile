.PHONY: test lint typecheck format

test:
	pytest

lint:
	ruff check .

typecheck:
	mypy

format:
	ruff format .
