FROM python:3.12

WORKDIR /app

RUN pip install uv

COPY ./pyproject.toml ./pyproject.toml
COPY ./uv.lock ./uv.lock

RUN uv sync

COPY ./migrations ./migrations
COPY ./alembic.ini ./alembic.ini

COPY ./web.py ./web.py
COPY ./entrypoint.sh ./entrypoint.sh
COPY ./src ./src

USER root

ENTRYPOINT [ "./entrypoint.sh" ]