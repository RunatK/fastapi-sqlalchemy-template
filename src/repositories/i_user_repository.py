from src.entities.user import DUser
from .dto.user import UserCreateDTO, UserUpdateDTO
from .i_base import IBaseRepository


class IUserRepository(IBaseRepository[DUser, int, UserCreateDTO, UserUpdateDTO]):
    pass
