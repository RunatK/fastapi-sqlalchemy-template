from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
import uvicorn

from src.core import config
from src.app.controllers.user import user_router as user_router


app = FastAPI(
    # Конфигурируем название проекта. Оно будет отображаться в документации
    title=config.PROJECT_NAME,
    # Адрес документации в красивом интерфейсе
    docs_url="/api/openapi",
    # Адрес документации в формате OpenAPI
    openapi_url="/api/openapi.json",
    # Можно сразу сделать небольшую оптимизацию сервиса
    # и заменить стандартный JSON-сериализатор на более шуструю версию, написанную на Rust
    default_response_class=ORJSONResponse,
)

app.include_router(user_router, prefix="/v1", tags=["users"])

if __name__ == "__main__":
    # Приложение может запускаться командой
    # `uvicorn main:app --host localhost --port 8080`
    # но чтобы не терять возможность использовать дебагер,
    # запустим uvicorn сервер через python
    uvicorn.run(
        "web:app", host=config.PROJECT_HOST, port=config.PROJECT_PORT, reload=True
    )
