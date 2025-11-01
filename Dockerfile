FROM python:3.12 AS build

WORKDIR /app

RUN pip install uv

COPY ./pyproject.toml ./pyproject.toml
COPY ./uv.lock ./uv.lock

RUN uv sync

COPY ./src ./src
COPY ./migrations ./migrations
COPY ./alembic.ini ./alembic.ini
FROM python:3.12

WORKDIR /app

COPY --from=build app/.venv ./.venv
COPY --from=build app/src ./src

USER root

ENTRYPOINT [ "./entrypoint.sh" ]