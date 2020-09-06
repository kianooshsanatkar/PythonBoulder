from abc import ABC, abstractmethod
from copy import copy

from core.datahandler.repository import GenericRepository
from core.exceptionhandler.exceptions import AuthorizationException
from core.resource.resource import ResourceManager, Texts


class BaseCQRS(ABC):
    __data_handler__: GenericRepository

    def __init__(self, user, data_handler: GenericRepository):
        self.__data_handler__ = data_handler
        self.__user = user

    @property
    def current_user(self):
        return copy(self.__user)

    def authorize(self) -> bool:
        if self.current_user is not None:
            return True
        return False

    @abstractmethod
    def run(self, *args):
        ...

    def execute(self, *args):
        if self.authorize() is True:
            return self.run(*args)
        else:
            raise AuthorizationException(ResourceManager.translate(Texts.USER_HAS_NOT_ACCESS))


class BaseCommand(BaseCQRS, ABC):
    pass


class BaseQuery(BaseCQRS, ABC):
    pass
