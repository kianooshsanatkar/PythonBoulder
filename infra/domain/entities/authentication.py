from core.auxiliary.helper import is_hashed
from infra.domain.entities.user import User


class AuthInfo(User):

    def __init__(self, uid=None, user_name=None, state=None, password=None):
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
