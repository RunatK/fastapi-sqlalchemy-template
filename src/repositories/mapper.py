from typing import Protocol

from src.entities.base import DEntity


class IMapper[M, E: DEntity](Protocol):
    @classmethod
    def to_entity(cls, model: M) -> E: ...

    @classmethod
    def to_model(cls, entity: E) -> M: ...
