import os
from logging import config as logging_config

from .logger import LOGGING

# Применяем настройки логирования
logging_config.dictConfig(LOGGING)

# Название проекта. Используется в Swagger-документации
PROJECT_NAME = os.getenv("PROJECT_NAME", "FastAPI & SQLAlchemy template")
PROJECT_HOST = os.getenv("PROJECT_HOST", "localhost")
PROJECT_PORT = int(os.getenv("PROJECT_PORT", "8000"))

DEBUG = os.getenv("DEBUG", False)

# База данных
DB_HOST = os.getenv("POSTGRES_HOST", "localhost")
DB_PORT = os.getenv("POSTGRES_PORT", 5432)
DB_NAME = os.getenv("POSTGRES_DB", "postgres")
DB_USER_NAME = os.getenv("POSTGRES_USER", "postgres")
DB_USER_PASSWORD = os.getenv("POSTGRES_PASSWORD", "postgres")
DB_ENGINE = os.getenv("POSTGRES_ENGINE", "postgresql+asyncpg")
DB_DSN = (
    f"{DB_ENGINE}://{DB_USER_NAME}:{DB_USER_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

STATIC_DIR = os.getenv("STATIC_DIR", "static")

CONNECTED_SERVERS = {
    "postgres": {
        "host": DB_HOST,
        "port": DB_PORT,
    },
}

# Корень проекта
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# CORS
ORIGINS = (
    f"https://{PROJECT_HOST}:{PROJECT_PORT}",
    f"http://{PROJECT_HOST}:{PROJECT_PORT}",
    f"http://{PROJECT_HOST}:81",
    f"http://{PROJECT_HOST}",
    f"https://{PROJECT_HOST}",
)
