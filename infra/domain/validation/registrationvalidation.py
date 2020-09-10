from core.auxiliary.helper import email_validator, extract_numbers, mobile_number_validator
from conventions import Email, CellPhone
from domain.entities.Registration import RegistrationInfo
from core.exceptionhandler.exceptions import ValidationException
from infra.resource import ResourceManager, Texts


def email_validation(email: Email) -> None:
    email_str = str(email).lower()
    if not email_validator(email_str):
        raise ValidationException(ResourceManager.translate(Texts.EMAIL_NOT_VALID))


def cellphone_validation(cellphone: CellPhone) -> None:
    if not mobile_number_validator(str(cellphone)):
        raise ValidationException(ResourceManager.translate(Texts.MOBILE_NOT_VALID))


def registration_validation(user: RegistrationInfo):
    if not user.email and not user.cellphone:
        raise ValidationException(ResourceManager.translate(Texts.USER_NEED_CONTACT))
    if user.email:
        user.cellphone.read(extract_numbers(str(user.cellphone)))
        email_validation(user.email)
    if user.cellphone:
        cellphone_validation(user.cellphone)
