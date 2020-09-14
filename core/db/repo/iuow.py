from abc import ABC, abstractmethod


class IUnitOfWork(ABC):

    def __init__(self, context):
        self.__context__ = context

    @abstractmethod
    def complete(self):
        pass

