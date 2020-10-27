from core.exceptionhandler.exceptions import AuthenticationException
from infra.auxiliary.helper import hash_match, hashing_string
from infra.domain.entities.authentication import AuthInfo
from infra.domain.entities.user import UserState
from infra.domain.validation import auth_validation
from infra.domain.validation.authvalidation import password_validation
from infra.resource import ResourceManager, Texts


def password_verification(auth: AuthInfo, password: str) -> None:
    if hash_match(auth.password, password) is not True:
        raise AuthenticationException(ResourceManager.translate(Texts.LOGIN_VALUE_INCORRECT))


def new_password(password: str):
    password_validation(password)
    return hashing_string(password)


def create_user_auth(username: str, state: UserState, password: str) -> AuthInfo:
    auth = AuthInfo(None, username.lower(), state, new_password(password))
    auth_validation(auth)
    return auth
