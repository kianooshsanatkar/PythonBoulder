from infra.domain.entities.Registration import RegistrationInfo
from infra.domain.entities.authentication import AuthInfo
from infra.domain.entities.user import User
from infra.domain.validation.authvalidation import password_validation
from infra.domain.validation.registrationvalidation import registration_validation
from infra.domain.validation.uservalidation import username


def user(auth_info: AuthInfo):
    username(User(auth_info))
    password_validation(auth_info.password)


def registration(r: RegistrationInfo):
    registration_validation(r)
