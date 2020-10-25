from infra.auxiliary import helper
from core.exceptionhandler.exceptions import ValidationException
from infra.domain.entities.authentication import AuthInfo
from infra.resource import ResourceManager, Texts


def password_validation(auth: AuthInfo, password: str = None):
    if helper.password_validation(auth.password if password is None else password) is not True:
        raise ValidationException(ResourceManager.translate(Texts.PASSWORD_VALUE_NOT_VALID))


