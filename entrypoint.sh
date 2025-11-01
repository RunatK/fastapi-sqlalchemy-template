#!/bin/bash
uv run alembic upgrade head;
uv run python ./web.py;