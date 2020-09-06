from core.auxiliary.helper import *
from core.domain.baseentity import Entity
from core.exceptions import ValidationException, AuthenticationException
from infra.resource import Texts, ResourceManager
from infra.domain.valueobject import UserState


class User(Entity):
    state: UserState
    user_name: str
    __password: str
    email: str
    email_verified: bool
    mobile_number: str
    mobile_verified: bool
    __hide_password = False
    __current_person__ = None
    persons = None

    @property
    def password(self):
        # return '' if self.__hide_password is True else self.__password
        return self.__password

    def __init__(self, id=None, user_name=None, password=None, email=None, mobile_number=None,
                 state=UserState.REGISTERED, email_verified=False, mobile_verified=False, persons=None,
                 current_person=None):
        super().__init__(id)
        self.user_name = user_name
        if password is not None:
            if is_hashed(password):
                self.__password = password
            else:
                self.set_new_password(password)
        self.email = email
        self.mobile_number = mobile_number
        self.state = state
        self.email_verified = email_verified
        self.mobile_verified = mobile_verified
        self.persons = persons
        self.__current_person__ = current_person

    def password_hidden(self,hide):
        self.__hide_password = hide

    def validation(self) -> None:
        self.username_validation()
        self.password_validation(self.password)
        if not self.email and not self.mobile_number:
            raise ValidationException(ResourceManager.translate(Texts.USER_NEED_CONTACT))
        if self.email:
            self.email_validation()
        if self.mobile_number:
            self.mobile_validation()

    def email_validation(self) -> None:
        self.email = self.email.lower()
        if not email_validator(self.email):
            raise ValidationException(ResourceManager.translate(Texts.EMAIL_NOT_VALID))

    def mobile_validation(self) -> None:
        self.mobile_number = extract_numbers(self.mobile_number)
        if not mobile_number_validator(self.mobile_number):
            raise ValidationException(ResourceManager.translate(Texts.MOBILE_NOT_VALID))

    def username_validation(self) -> None:
        self.user_name = self.user_name.lower()
        self.user_name = self.user_name.lower()
        if not username_validation(self.user_name):
            raise ValidationException(ResourceManager.translate(Texts.USER_NAME_NOT_VALID))

    def set_new_password(self, password: str):
        self.password_validation(password)
        self.__password = hashing_string(password)

    def password_validation(self, password: str=None):
        if password_validation(self.password if password is None else password) is not True:
            raise ValidationException(ResourceManager.translate(Texts.PASSWORD_VALUE_NOT_VALID))

    def password_verification(self, password: str) -> None:
        if hash_match(self.__password, password) is not True:
            raise AuthenticationException(ResourceManager.translate(Texts.LOGIN_VALUE_INCORRECT))


# todo: class UserSecurity(Entity):
class UserSecurity(Entity):
    pass
