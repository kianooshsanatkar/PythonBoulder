from exceptionhandler.exceptions import ValidationException
from infra.domain.entities.user import User
from infra.resource import ResourceManager, Texts


def __username_validation(user: User) -> None:
    user.user_name = user.user_name.lower()
    user.user_name = user.user_name.lower()
    if not __username_validation(user.user_name):
        raise ValidationException(ResourceManager.translate(Texts.USER_NAME_NOT_VALID))


def validation(user: User) -> None:
    __username_validation(user)
