from src.entities.user import DUser
from src.repositories.mapper import IMapper
from src.app.db.models.user import User


class UserMapper(IMapper[User, DUser]):
    @classmethod
    def to_entity(cls, model: User) -> DUser:
        return DUser(
            id_=model.id_,
            username=model.username,
            password=model.password,
            name=model.name,
            surname=model.surname,
            patronymic=model.patronymic,
        )

    @classmethod
    def to_model(cls, entity: DUser) -> User:
        return User(
            id_=entity.id_,
            username=entity.username,
            password=entity.password,
            name=entity.name,
            surname=entity.surname,
            patronymic=entity.patronymic,
        )
