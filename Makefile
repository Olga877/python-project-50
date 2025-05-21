install:
	uv sync

uninstall:
	uv tool uninstall hexlet-code

reinstall:
	uv tool install --force dist/*.whl

test-coverage:
	uv run pytest --cov=gendiff --cov-report=xml:coverage.xml


build:
	uv build

package-install:
	uv tool install dist/*.whl

run:
	uv run hexlet-python-package

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=hexlet_python_package --cov-report xml

lint:
	uv run ruff check

check: test lint

.PHONY: install test lint selfcheck check build