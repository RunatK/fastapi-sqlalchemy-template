from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase


class Model:
    pass


# Базовый класс для всех моделей
class BaseModel(AsyncAttrs, DeclarativeBase):
    __abstract__ = True
