#!/bin/sh -e

docker compose -f docker/compose.yml --env-file .env up --detach --remove-orphans

poetry install
poetry run alembic upgrade head
