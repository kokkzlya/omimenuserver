FROM python:3.12-slim AS base

WORKDIR /opt/app
RUN pip install poetry
RUN apt update && apt install -y libsodium23
COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false \
    && poetry install


FROM base AS init

COPY ./alembic     /opt/app/alembic
COPY ./src         /opt/app/src
COPY ./alembic.ini /opt/app/

ENV PYTHONPATH=/opt/app/src
ENV PYTHONBUFFERED=1


FROM base

COPY ./src       /opt/app/src
COPY ./manage.sh /opt/app/

ENV PYTHONBUFFERED=1
ENTRYPOINT ["/opt/app/manage.sh"]
