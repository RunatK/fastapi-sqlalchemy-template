from typing import Annotated

from fastapi import APIRouter, Body, Path, status

from src.entities.user import DUser
from src.repositories.dto.user import UserCreateDTO, UserUpdateDTO
from src.app.di import AsyncDBSessionDepends
from src.app.db.repositories.user import UserRepository

user_router = APIRouter(
    dependencies=[]  # there are can be placed methods of authZ
)


@user_router.get("/users/")
async def get(session: AsyncDBSessionDepends) -> list[DUser]:
    repository = UserRepository(session=session)
    return await repository.get()


@user_router.post("/users/", status_code=status.HTTP_201_CREATED)
async def create(dto: UserCreateDTO, session: AsyncDBSessionDepends) -> DUser:
    repository = UserRepository(session=session)
    result = await repository.create(dto)
    await session.commit()
    return result


@user_router.put("/users/{user_id}/")
async def update(
    user_id: Annotated[int, Path()],
    dto: Annotated[UserUpdateDTO, Body()],
    session: AsyncDBSessionDepends,
) -> DUser:
    repository = UserRepository(session=session)
    result = await repository.update(user_id, dto)
    await session.commit()
    return result


@user_router.delete("/users/{user_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete(
    user_id: Annotated[int, Path()], session: AsyncDBSessionDepends
) -> None:
    repository = UserRepository(session=session)
    await repository.delete(user_id)
    await session.commit()
