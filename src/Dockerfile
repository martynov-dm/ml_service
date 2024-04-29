FROM python:3.12.2-slim-bookworm

# Install Poetry
RUN pip install poetry==1.8.2
RUN pip install poethepoet==0.25.1

# Set Poetry environment variables
ENV POETRY_HOME=/opt/poetry \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH=/opt/poetry/libpython \
    PATH="$POETRY_HOME/bin:$PATH"

ENV DOCKER_ENV=1

# Create a new poetry project
WORKDIR /app

# Copy project files
COPY pyproject.toml poetry.lock ./

# Install dependencies
RUN poetry install --without dev --no-root && rm -rf $POETRY_CACHE_DIR

# Copy source code
COPY src ./src

# Set PYTHONPATH
ENV PYTHONPATH=/app/src:"$PYTHONPATH"

# Entrypoint
ENTRYPOINT ["poe", "api"]