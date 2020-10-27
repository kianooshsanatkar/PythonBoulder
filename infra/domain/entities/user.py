from enum import Enum
from uuid import UUID

from core.domain.baseentity import Entity


class UserState(Enum):
    INITIALIZED = 1
    REGISTERED = 10
    ACTIVATED = 20
    DEACTIVATED = 30
    SUSPENDED = 40


class User(Entity):

    def __init__(self, uid: UUID = None, username: str = None, state: UserState = None):
        super().__init__(uid)
        self.username = username
        self.state = state


# todo: class UserSecurity(Entity):
class UserSecurity(Entity):
    pass
