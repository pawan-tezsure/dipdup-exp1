FROM python:3.9-slim-buster

RUN pip install poetry

WORKDIR /demo
COPY poetry.lock pyproject.toml /demo/
COPY . /demo


ENTRYPOINT ["poetry", "run", "dipdup"]
CMD ["-c", "dipdup.yml", "run"]

