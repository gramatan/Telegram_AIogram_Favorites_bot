FROM python:3.10-slim AS builder

RUN apt-get update && apt-get install -y \
    curl \
    build-essential \
    && apt-get clean

RUN curl -sSL https://install.python-poetry.org | python3 - \
    && mv /root/.local/bin/poetry /usr/local/bin/poetry

WORKDIR /build

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false && poetry install --no-dev

COPY async_bot async_bot

FROM python:3.10-slim

WORKDIR /async_bot

COPY --from=builder /build/async_bot .
COPY --from=builder /build/pyproject.toml ./pyproject.toml
COPY --from=builder /build/poetry.lock ./poetry.lock

COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /usr/local/bin/poetry /usr/local/bin/poetry

ENV PYTHONPATH=/async_bot

CMD ["python", "app.py"]
