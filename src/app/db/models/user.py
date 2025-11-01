from sqlalchemy.orm import Mapped, MappedColumn
from sqlalchemy import Integer, String

from .base import BaseModel, Model


class User(BaseModel, Model):
    __tablename__ = "users"

    id_: Mapped[int] = MappedColumn(Integer, autoincrement=True, primary_key=True)
    username: Mapped[str] = MappedColumn(String(255))
    password: Mapped[str] = MappedColumn(String(127))

    name: Mapped[str] = MappedColumn(String(255))
    surname: Mapped[str] = MappedColumn(String(255))
    patronymic: Mapped[str] = MappedColumn(String(255))

    def __repr__(self) -> str:
        return str(self.id_)
