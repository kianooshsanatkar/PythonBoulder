from abc import ABCMeta, abstractmethod


class AbsRepository(metaclass=ABCMeta):
    # Todo: translator Trade-off: where does it belong?
    # def __init__(self, translator):
    #     self.__translator__ = translator

    @abstractmethod
    def add(self, entity):
        pass

    @abstractmethod
    def add_range(self, entities):
        pass

    @abstractmethod
    def remove(self, entity):
        pass

    @abstractmethod
    def remove_range(self, entities):
        pass

    @abstractmethod
    def get(self, uid):
        pass

    @abstractmethod
    def get_all(self, start, count):
        pass

    @abstractmethod
    def find(self):
        pass

    @abstractmethod
    def find_all(self):
        pass
