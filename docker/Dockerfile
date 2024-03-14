FROM python:3.12.2-slim-bullseye

RUN mkdir service/src
RUN mkdir service/tests
COPY ../src service/src
COPY ../tests service/tests
COPY ../pyproject.toml service
COPY ../poetry.lock service
COPY ../Makefile service
COPY ../.pylintrc service
WORKDIR service
RUN pip install poetry
RUN poetry install
RUN make protogen

EXPOSE 50051
ENTRYPOINT [ "python", "recommendations.py" ]