from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.repositories.i_user_repository import IUserRepository
from src.app.db.repositories.user import UserRepository
from .db.session import get_session


AsyncDBSessionDepends = Annotated[AsyncSession, Depends(get_session)]


async def get_user_repository(session: AsyncDBSessionDepends) -> IUserRepository:
    return UserRepository(session)

UserRepositoryDepends = Annotated[IUserRepository, Depends(get_user_repository)]