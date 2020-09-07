from core.auxiliary.helper import *
from core.domain.baseentity import Entity
from core.exceptionhandler.exceptions import ValidationException, AuthenticationException
from domain.ConventionalObjects import Email, CellPhone
from infra.resource import Texts, ResourceManager
from infra.domain.valueobject import UserState


class User(Entity):

    def __init__(self, uid=None, user_name=None, state=UserState.REGISTERED):
        super().__init__(uid)
        self.user_name = user_name
        self.state = state


class AuthInfo(User):
    __hide_password = False

    def __init__(self, uid=None, user_name=None, state=UserState.REGISTERED, password=None):
        super().__init__(uid, user_name, state)
        if password is not None:
            if is_hashed(password):
                self.__password = password
            else:
                self.set_new_password(password)

    @property
    def password(self):
        # return '' if self.__hide_password is True else self.__password
        return self.__password

    def password_hidden(self, hide):
        self.__hide_password = hide

    def set_new_password(self, password: str):
        self.password_validation(password)
        self.__password = hashing_string(password)

    def password_validation(self, password: str = None):
        if password_validation(self.password if password is None else password) is not True:
            raise ValidationException(ResourceManager.translate(Texts.PASSWORD_VALUE_NOT_VALID))

    def password_verification(self, password: str) -> None:
        if hash_match(self.__password, password) is not True:
            raise AuthenticationException(ResourceManager.translate(Texts.LOGIN_VALUE_INCORRECT))

    def validation(self):
        self.password_validation(self.password)


class RegistrationInfo(User):

    def __init__(self, uid=None, user_name=None, state=UserState.REGISTERED, email: Email = None,
                 cellphone: CellPhone = None, persons=None, current_person=None):
        super().__init__(uid, user_name, state)
        self.cellphone = cellphone
        self.email = email
        self.persons = persons
        self.current_person = current_person


# todo: class UserSecurity(Entity):
class UserSecurity(Entity):
    pass
