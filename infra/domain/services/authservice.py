from auxiliary.helper import hash_match, hashing_string
from infra.domain.validation.authvalidation import password_validation
from exceptionhandler.exceptions import AuthenticationException
from domain.entities.authentication import AuthInfo
from infra.resource import ResourceManager, Texts


def password_verification(auth:AuthInfo, password: str) -> None:
    if hash_match(auth.password, password) is not True:
        raise AuthenticationException(ResourceManager.translate(Texts.LOGIN_VALUE_INCORRECT))


def set_new_password(self, password: str):
    password_validation(password)
    self.__password = hashing_string(password)
