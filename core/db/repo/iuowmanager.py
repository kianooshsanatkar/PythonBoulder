from abc import abstractmethod, ABC


class IUnitOfWorkConfiguration(ABC):

    @abstractmethod
    def get_context(self):
        raise NotImplementedError()
