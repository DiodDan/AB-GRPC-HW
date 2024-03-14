FROM python:3.12.2-slim-bullseye
RUN mkdir service
WORKDIR service
RUN mkdir src
RUN mkdir tests
COPY ../src src
COPY ../tests tests
COPY ../pyproject.toml .
COPY ../poetry.lock .
COPY ../Makefile .
COPY ../.pylintrc .
RUN pip install poetry
RUN apt update && apt install -y make
RUN make install

RUN pip list
RUN ls
RUN poetry show --tree
RUN poetry run make protogen

EXPOSE 5000
ENTRYPOINT [ "poetry", "run", "python", "src/greeting/client.py" ]