all: .venv lint pylint build

.venv: poetry.lock
	@poetry install --with ci --sync
	@touch .venv

.PHONY: format
format: .venv
	@poetry run ruff format
	@poetry run ruff check --select I --fix

.PHONY: lint
lint: .venv
	@poetry run ruff check $(if $(FIX),--fix)
	@poetry run ruff format --diff
	@poetry run ruff check --select I

.PHONY: pylint
pylint: .venv
	@poetry run pylint httpie_hush* -E

.PHONY: build
build:
	@poetry build

.PHONY: publish
publish:
	@poetry publish
