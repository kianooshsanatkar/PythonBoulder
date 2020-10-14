from enum import Enum

from core.domain.baseentity import Entity


class UserState(Enum):
    INITIALIZED = 1
    REGISTERED = 10
    ACTIVATED = 20
    DEACTIVATED = 30
    SUSPENDED = 40


class User(Entity):

    def __init__(self, uid=None, user_name=None, state=None):
        super().__init__(uid)
        self.user_name = user_name
        self.state = state


# todo: class UserSecurity(Entity):
class UserSecurity(Entity):
    pass
