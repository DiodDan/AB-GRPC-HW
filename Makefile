CODE_FOLDERS := src
TEST_FOLDERS := tests
PROTO_FOLDER := ./$(CODE_FOLDERS)/protobufs

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

protogen:
	python -m grpc_tools.protoc -I $(PROTO_FOLDER) --python_out=$(CODE_FOLDERS)/greeting --grpc_python_out=$(CODE_FOLDERS)/greeting $(PROTO_FOLDER)/service.proto
	black $(CODE_FOLDERS)