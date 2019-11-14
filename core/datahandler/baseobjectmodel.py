import uuid

from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import UUID


class BaseObjectModel():
    __tablename__: str
    Id = Column(UUID(as_uuid=True), default=uuid.uuid4(), primary_key=True)

    def __init__(self, Id = None):
        if Id is not None and isinstance(Id, uuid.UUID):
            self.Id = Id
