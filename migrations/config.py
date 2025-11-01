import os


DB_HOST = os.getenv("POSTGRES_HOST", "localhost")
DB_PORT = os.getenv("POSTGRES_PORT", 5432)
DB_NAME = os.getenv("POSTGRES_DB", "postgres")
DB_USER_NAME = os.getenv("POSTGRES_USER", "postgres")
DB_USER_PASSWORD = os.getenv("POSTGRES_PASSWORD", "postgres")
DB_ENGINE = os.getenv("POSTGRES_ENGINE", "postgresql+asyncpg")
DB_DSN = (
    f"{DB_ENGINE}://{DB_USER_NAME}:{DB_USER_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
