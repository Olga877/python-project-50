install:
	uv sync
uninstall:
	uv tool uninstall hexlet-code
build:
	uv build
package-install:
	uv tool install dist/*.whl
lint:
	uv run ruff check gendiff