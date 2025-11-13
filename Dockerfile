FROM python:3.11-slim-bullseye as python-base

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.8.3 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv" \
    DEBIAN_FRONTEND=noninteractive

ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

# Dependências do sistema
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        curl \
        build-essential \
        gcc \
        libpq-dev \
        python3-dev && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Instalar Poetry moderno (sem cache antigo)
RUN curl -sSL https://install.python-poetry.org | python3 - && \
    ln -s /opt/poetry/bin/poetry /usr/local/bin/poetry

# Configurar ambiente do projeto
WORKDIR $PYSETUP_PATH

COPY poetry.lock pyproject.toml ./

# Evita criação de virtualenv separada
RUN poetry config virtualenvs.create false

# Instala apenas dependências principais
RUN poetry install --no-root --without dev

# Copia o restante do projeto
WORKDIR /app
COPY . /app/

EXPOSE 8080

CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
