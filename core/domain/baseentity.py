from abc import ABC
import uuid


class Entity(ABC):
    uid: uuid.UUID

    def __init__(self, uid=None):
        if uid is None:
            self.uid = uuid.uuid4()
        else:
            self.uid = uid

    # @property
    # def entity_id(self):
    #     return self.id
