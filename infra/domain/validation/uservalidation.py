from infra.auxiliary.helper import username_validation
from exceptionhandler.exceptions import ValidationException
from infra.resource import ResourceManager, Texts


def username(user_name: str) -> None:
    if not username_validation(user_name):
        raise ValidationException(ResourceManager.translate(Texts.USER_NAME_NOT_VALID))
