from exceptionhandler.exceptions import ValidationException
from core.auxiliary.helper import username_validation
from infra.domain.entities.user import User
from infra.resource import ResourceManager, Texts


def username(user: User) -> None:
    user.user_name = user.user_name.lower()
    user.user_name = user.user_name.lower()
    if not username(user.user_name):
        raise ValidationException(ResourceManager.translate(Texts.USER_NAME_NOT_VALID))
