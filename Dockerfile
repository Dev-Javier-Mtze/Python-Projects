# Stage 1: Builder
FROM python:3.11-slim AS builder

RUN pip install poetry

WORKDIR /app

COPY pyproject.toml poetry.lock ./

# Install dependencies into the builder environment
RUN poetry install --no-root --only main

COPY src ./src

# Stage 2: Final image
FROM python:3.11-slim

WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /usr/local /usr/local
COPY src ./src

EXPOSE 8000

CMD ["uvicorn", "poetry_demo.main:app", "--host", "0.0.0.0", "--port", "8000"]
