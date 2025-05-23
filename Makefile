CODE_FOLDERS := src
TEST_FOLDERS := tests
PROTO_FOLDER := ./$(CODE_FOLDERS)/protobufs

.PHONY: test lint format

install:
	poetry install --no-root

test:
	poetry run pytest tests

format:
	black $(TEST_FOLDERS)
	black $(CODE_FOLDERS)

lint:
	black --check $(TEST_FOLDERS)
	black --check $(CODE_FOLDERS)

protogen:
	poetry run python -m grpc_tools.protoc -I $(PROTO_FOLDER) --python_out=$(CODE_FOLDERS)/greeting --grpc_python_out=$(CODE_FOLDERS)/greeting $(PROTO_FOLDER)/service.proto
	black $(CODE_FOLDERS)

test_on_docker:
	docker-compose up test