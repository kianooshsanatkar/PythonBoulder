from abc import ABC, abstractmethod
from copy import copy

from core.exceptionhandler.exceptions import AuthorizationException
from core.resource.resource import ResourceManager, Texts


class BaseCQRS(ABC):

    def __init__(self, user, uow):
        self.__uow__ = uow
        self.__user__ = user

    @property
    def current_user(self):
        return copy(self.__user__)

    def authorize(self) -> bool:
        if self.current_user is not None:
            return True
        return False

    @abstractmethod
    def run(self, *args, **kwargs):
        ...

    def execute(self, *args, **kwargs):
        if self.authorize() is True:
            return self.run(*args, **kwargs)
        else:
            raise AuthorizationException(ResourceManager.translate(Texts.USER_HAS_NOT_ACCESS))


class BaseCommand(BaseCQRS, ABC):
    pass


class BaseQuery(BaseCQRS, ABC):
    pass
