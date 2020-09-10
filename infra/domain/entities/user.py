from core.auxiliary.helper import is_hashed, hash_match
from core.domain.baseentity import Entity
from core.exceptionhandler.exceptions import ValidationException, AuthenticationException
from domain.ConventionalObjects import Email, CellPhone
from infra.resource import Texts, ResourceManager
from infra.domain.valueobject import UserState


class User(Entity):

    def __init__(self, uid=None, user_name=None, state=UserState.DEACTIVATE):
        super().__init__(uid)
        self.user_name = user_name
        self.state = state


class AuthInfo(User):

    def __init__(self, uid=None, user_name=None, state=UserState.DEACTIVATE, password=None):
        super().__init__(uid, user_name, state)
        if password is not None:
            self.password = password

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if isinstance(value, str):
            if is_hashed(value):
                self.__password = value
                return

        raise ValueError("password must be a hashed")


class RegistrationInfo(User):

    def __init__(self, uid=None, user_name=None, state=UserState.DEACTIVATE, email: Email = None,
                 cellphone: CellPhone = None, persons=None, current_person=None):
        super().__init__(uid, user_name, state)
        self.cellphone = cellphone
        self.email = email
        self.persons = persons
        self.current_person = current_person


# todo: class UserSecurity(Entity):
class UserSecurity(Entity):
    pass
