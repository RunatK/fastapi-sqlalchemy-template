from typing import Protocol

from pydantic import BaseModel


class IBaseRepository[Entity, IDKey, CreateDTO: BaseModel, UpdateDTO: BaseModel](
    Protocol
):
    async def get(self, *args, **kwargs) -> list[Entity]:
        """
        Get all entities
        """
        ...

    async def get_by(self, id: IDKey, *args, **kwargs) -> Entity:
        """
        Get entity by id
        """
        ...

    async def update(self, id: IDKey, dto: UpdateDTO, *args, **kwargs) -> Entity:
        """
        Update entity by id. DTO represent fields that can be updated
        """
        ...

    async def create(self, dto: CreateDTO, *args, **kwargs) -> Entity:
        """
        Cread entity from dto
        """
        ...

    async def delete(self, id: IDKey, *args, **kwargs) -> None:
        """
        Delete entity by id
        """
        ...
