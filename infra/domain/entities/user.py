from core.domain.baseentity import Entity
from infra.domain.valueobject import UserState


class User(Entity):

    def __init__(self, uid=None, user_name=None, state=UserState.DEACTIVATE):
        super().__init__(uid)
        self.user_name = user_name
        self.state = state


# todo: class UserSecurity(Entity):
class UserSecurity(Entity):
    pass
