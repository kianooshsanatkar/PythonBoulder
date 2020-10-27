from core.exceptionhandler.exceptions import ValidationException
from infra.auxiliary import helper
from infra.resource import ResourceManager, Texts


def password_validation(password: str = None):
    if helper.password_validation(password) is not True:
        raise ValidationException(ResourceManager.translate(Texts.PASSWORD_VALUE_NOT_VALID))
