from uuid import UUID
from abc import ABC, abstractmethod
from core.domain.baseentity import Entity


class BaseDataHandler(ABC):

    @abstractmethod
    def get_by_id(self,entity_type: type , id: UUID)->Entity: ...

    @abstractmethod
    def get(self, entity: Entity)-> Entity: ...

    # @abstractmethod
    # def get_all(self)-> [Entity]: ...

    @abstractmethod
    def insert(self, entity: Entity): ...

    @abstractmethod
    def update(self, entity: Entity): ...

    @abstractmethod
    def delete(self, entity: Entity): ...
