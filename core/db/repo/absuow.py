from abc import ABC, abstractmethod


class AbsUnitOfWork(ABC):

    def __init__(self, context):
        self.__context__ = context

    @abstractmethod
    def commit(self):
        pass

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def close(self):
        pass

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
