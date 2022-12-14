.DEFAULT_GOAL := help

.PHONY: help
help:  ## Show this help.
	@grep -E '^\S+:.*?## .*$$' $(firstword $(MAKEFILE_LIST)) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "%-30s %s\n", $$1, $$2}'

.PHONY: local-setup
local-setup: ## Set up the local environment (e.g. install git hooks)
	scripts/local-setup.sh

.PHONY: install
install: ## Install all dependencies
	poetry install

.PHONY: update
update: ## Update dependencies
	poetry update

.PHONY: check-typing
check-typing:  ## Run a static analyzer over the code to find issues
	poetry run mypy .

.PHONY: check-format
check-format:
	poetry run black --check .

.PHONY: check-imports
check-imports:
	poetry run isort --diff .

.PHONY: check-style
check-style:
	poetry run flake8 .
	poetry run pylint ./*

.PHONY: reformat
reformat:  ## Format python code
	poetry run black .
	poetry run pyupgrade --py310-plus **/*.py
	poetry run isort .

.PHONY: test
test: ## Run all available tests
	PYTHONPATH=. poetry run pytest -n auto -m "not only_ci"

.PHONY: pre-commit
pre-commit: check-imports check-format check-typing check-style test
