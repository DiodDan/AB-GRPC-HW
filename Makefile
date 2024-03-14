CODE_FOLDERS := src
TEST_FOLDERS := tests

.PHONY: test lint format

install:
	poetry install --no-root

test:
	poetry run pytest

format:
	black $(TEST_FOLDERS)
	black $(CODE_FOLDERS)
	isort $(TEST_FOLDERS)
	isort $(CODE_FOLDERS)

lint:
	black --check $(TEST_FOLDERS)
	black --check $(CODE_FOLDERS)
	isort --check $(TEST_FOLDERS)
	isort --check $(CODE_FOLDERS)
	flake8 $(CODE_FOLDERS) $(TEST_FOLDERS)
	pylint $(CODE_FOLDERS) $(TEST_FOLDERS)
