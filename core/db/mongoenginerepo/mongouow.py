from abc import abstractmethod, ABC
from collections import namedtuple

from mongoengine import connection

from db.repo.absuow import AbsUnitOfWork


class BaseUnitOfWork(AbsUnitOfWork, ABC):

    def __init__(self, db=None, alias=None, host=None, port=None):
        Context = namedtuple('Context', ['db', 'alias', 'host', 'port'])
        super().__init__(Context(db, alias, host, port))

    def connect(self):
        connection.connect(self.__context__.db)

    def close(self):
        connection.disconnect(self.__context__.alias)

    @abstractmethod
    def commit(self):
        pass
