from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.repositories.dto.user import UserCreateDTO, UserUpdateDTO

from .mappers.user import UserMapper

from src.entities.user import DUser
from src.repositories.i_user_repository import IUserRepository
from src.app.db.models.user import User


class UserRepository(IUserRepository):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__()
        self._session = session

    async def get(self, *args, **kwargs) -> list[DUser]:
        stmt = select(User)
        return [
            UserMapper.to_entity(user)
            for user in (await self._session.scalars(stmt)).all()
        ]

    async def get_by(self, id: int, *args, **kwargs) -> DUser:
        stmt = select(User).where(User.id_ == id)
        return UserMapper.to_entity((await self._session.scalars(stmt)).one())

    async def update(self, id: int, dto: UserUpdateDTO, *args, **kwargs) -> DUser:
        user = await self.get_by(id=id)
        if dto.password is not None:
            user.password = dto.password
        if dto.name is not None:
            user.name = dto.name
        if dto.surname is not None:
            user.surname = dto.surname
        if dto.patronymic is not None:
            user.patronymic = dto.patronymic
        new_user = UserMapper.to_model(user)
        await self._session.merge(new_user)
        await self._session.flush()
        return UserMapper.to_entity(new_user)

    async def create(self, dto: UserCreateDTO, *args, **kwargs) -> DUser:
        user = User(
            username=dto.username,
            password=dto.password,
            name=dto.name,
            surname=dto.surname,
            patronymic=dto.patronymic,
        )
        self._session.add(user)
        await self._session.flush()
        return UserMapper.to_entity(user)

    async def delete(self, id: int, *args, **kwargs) -> None:
        user = await self.get_by(id=id)
        await self._session.delete(UserMapper.to_model(user))
        await self._session.flush()
