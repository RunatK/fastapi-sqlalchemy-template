from pydantic import BaseModel

from .base import DEntity


class DUser(BaseModel, DEntity):
    id_: int
    username: str
    password: str
    name: str
    surname: str
    patronymic: str
