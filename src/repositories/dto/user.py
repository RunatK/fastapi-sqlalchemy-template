from pydantic import BaseModel


class UserCreateDTO(BaseModel):
    username: str
    password: str
    name: str
    surname: str
    patronymic: str


class UserUpdateDTO(BaseModel):
    password: str | None = None
    name: str | None = None
    surname: str | None = None
    patronymic: str | None = None
