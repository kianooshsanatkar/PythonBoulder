from abc import ABC
import uuid


class Entity(ABC):
    id: uuid.UUID

    def __init__(self, id=None):
        if id is None:
            self.id = uuid.uuid4()
        else:
            self.id = id

    # @property
    # def entity_id(self):
    #     return self.id
