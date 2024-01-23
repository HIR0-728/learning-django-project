FROM python:3.11.1-slim-bullseye

COPY ./ /app
WORKDIR /app

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y \
        wget \
        curl \
        git \
        gcc \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install -U pip \
    && pip install poetry \
    && poetry run pip install -U pip setuptools \
    && poetry install --no-dev --no-interaction --no-ansi

ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1
ENV LANG ja_JP.UTF-8

RUN chmod +x /app/start.sh
CMD ["/app/start.sh"]