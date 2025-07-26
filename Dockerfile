FROM python:3.12.0-slim

ARG VIRTUAL_ENV=/usr/venv

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VERSION=2.1.3 \
    POETRY_HOME=/usr/local \
    POETRY_INSTALLER_MAX_WORKERS=4 \
    VIRTUAL_ENV=$VIRTUAL_ENV \
    PATH=$VIRTUAL_ENV/bin:$PATH

RUN apt-get update && \
    apt-get install -y python3-dev python3-venv python3-pip python3-wheel \
        redis-server apt-transport-https \
        libpq-dev git wget curl && \
    rm -rf /var/lib/apt/lists/* /var/cache/debconf && \
    apt-get clean && \
    curl -sSL https://install.python-poetry.org | python3 - && \
    python3 -m venv $VIRTUAL_ENV

WORKDIR /homme/django/dialog_backend
COPY pyproject.toml poetry.lock /
RUN poetry install --no-interaction --no-root --no-ansi
