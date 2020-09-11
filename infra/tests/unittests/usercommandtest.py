# Todo: Rewrite the whole test Again

"""
import uuid
from unittest import TestCase

from core.exceptionhandler.exceptions import ValidationException, AuthenticationException
from infra.domain.entities.Registration import RegistrationInfo
from infra.domain.entities.user import User, UserState
from infra.domain.validation.registrationvalidation import registration_validation


class UserCommandTest(TestCase):

    def user_builder(self):
        return RegistrationInfo(uuid.uuid4(), 'test_user', 'Passw0rd', 'test_email@email.com', "9121234567",
                                UserState.ACTIVE, True)

    def test_user_validation_email(self):
        user = self.user_builder()
        # must be Valid
        registration_validation(user)
        user.email = "test.test@test.test"
        registration_validation(user)
        user.email = "tt@ttt.tt"
        registration_validation(user)
        user.email = "1tt1@ttt.tt"
        registration_validation(user)
        user.email = "tt.tt_t@tt-t.tt"
        registration_validation(user)
        user.email = "t" * 313 + "@ttt.tt"
        registration_validation(user)

        # Not Valid
        user.email = "t" * 314 + "@ttt.tt"
        self.assertRaises(ValidationException, lambda: registration_validation(user))
        user.email = "t@ttt.tt"
        self.assertRaises(ValidationException, lambda: registration_validation(user))
        user.email = "tt@tt.tt"
        self.assertRaises(ValidationException, lambda: registration_validation(user))
        user.email = "tt@ttt.t"
        self.assertRaises(ValidationException, lambda: registration_validation(user))
        user.email = "tt@tttt..tt"
        self.assertRaises(ValidationException, lambda: registration_validation(user))
        user.email = "tt.@ttt.tt"
        self.assertRaises(ValidationException, lambda: registration_validation(user))
        user.email = "tt_@ttt.tt"
        self.assertRaises(ValidationException, lambda: registration_validation(user))
        user.email = "tt@tt_t.tt"
        self.assertRaises(ValidationException, lambda: registration_validation(user))
        user.email = "tt@ttt.t-t"
        self.assertRaises(ValidationException, lambda: registration_validation(user))
        user.email = "tt@ttt.t_t"
        self.assertRaises(ValidationException, lambda: registration_validation(user))
        user.email = ".tt@ttt.tt"
        self.assertRaises(ValidationException, lambda: registration_validation(user))
        user.email = "tt@ttt.tt."
        self.assertRaises(ValidationException, lambda: user.validation())

    def test_user_validation_phone(self):
        user = self.user_builder()
        user.validation()
        user.mobile_number = "9121234567"
        user.validation()
        user.mobile_number = "9301234567"
        user.validation()
        user.mobile_number = "09121234567"
        user.validation()
        user.mobile_number = "+989121234567"
        user.validation()

        user.mobile_number = "+989121+_}{[]';:/?.,akjdhf nca \'\"\\//><~!@#$`23456asdf7مشسنیتشبمدصشذثغ ريال,]ۀ«آۀژٍ"
        user.validation()

        user.mobile_number = ""
        user.validation()
        user.mobile_number = None
        user.validation()
        user.mobile_number = "1"
        self.assertRaises(ValidationException, lambda: user.validation())
        user.mobile_number = "123456789"
        self.assertRaises(ValidationException, lambda: user.validation())
        user.mobile_number = "0123456789"
        self.assertRaises(ValidationException, lambda: user.validation())
        user.mobile_number = "0912345678"
        self.assertRaises(ValidationException, lambda: user.validation())
        user.mobile_number = "+981234567890"
        self.assertRaises(ValidationException, lambda: user.validation())
        user.mobile_number = "912123456t"
        self.assertRaises(ValidationException, lambda: user.validation())
        user.mobile_number = "912-234567"
        self.assertRaises(ValidationException, lambda: user.validation())
        user.mobile_number = "912.234567"
        self.assertRaises(ValidationException, lambda: user.validation())

    def test_user_validation_no_contact(self):
        user = self.user_builder()
        user.mobile_number = ""
        user.email = ""
        self.assertRaises(ValidationException, lambda: user.validation())
        user.mobile_number = None
        user.email = None
        self.assertRaises(ValidationException, lambda: user.validation())

    def test_user_validation_username(self):
        user = self.user_builder()
        user.validation()
        user.user_name = "ttt"
        user.validation()
        user.user_name = "tt_t"
        user.validation()
        user.user_name = "t_t"
        user.validation()
        user.user_name = "tttttt"
        user.validation()
        user.user_name = "123"
        user.validation()
        user.user_name = "123"
        user.validation()

        user.user_name = ""
        self.assertRaises(ValidationException, lambda: user.validation())
        user.user_name = "t"
        self.assertRaises(ValidationException, lambda: user.validation())
        user.user_name = "tt"
        self.assertRaises(ValidationException, lambda: user.validation())
        user.user_name = "_ttt"
        self.assertRaises(ValidationException, lambda: user.validation())
        user.user_name = "ttt_"
        self.assertRaises(ValidationException, lambda: user.validation())
        user.user_name = "tt.t"
        self.assertRaises(ValidationException, lambda: user.validation())
        user.user_name = "tt-t"
        self.assertRaises(ValidationException, lambda: user.validation())
        user.user_name = "\"''][{}-0=-0/.شسیابتنب"
        self.assertRaises(ValidationException, lambda: user.validation())

    def test_user_set_and_verify_password(self):
        user = self.user_builder()
        password_str = "Passw0rd"
        user.set_new_password(password_str)
        user.password_verification(password_str)
        self.assertRaises(AuthenticationException, user.password_verification, "password")

    def test_user_password_validation(self):
        user = User()
        self.assertRaises(ValidationException, lambda: user.password_validation("password"))
        self.assertRaises(ValidationException, lambda: user.password_validation("password'"))
        self.assertRaises(ValidationException, lambda: user.password_validation("password\""))
        self.assertRaises(ValidationException, lambda: user.password_validation("pass'word"))
        self.assertRaises(ValidationException, lambda: user.password_validation("'password"))
        self.assertRaises(ValidationException, lambda: user.password_validation("\"password"))
        self.assertRaises(ValidationException, lambda: user.password_validation("pass\"word"))
        self.assertRaises(ValidationException, lambda: user.password_validation("passw0rd"))
        self.assertRaises(ValidationException, lambda: user.password_validation("Password"))
        self.assertRaises(ValidationException, lambda: user.password_validation("Pa$$0"))
        self.assertRaises(ValidationException, lambda: user.password_validation("Password"))
        user.password_validation("Pa$$word")
        user.password_validation("Passw0rd")
        user.password_validation("Pa$$w0rd")
        user.password_validation("Password1234567890-=_+")
        user.password_validation("Pas`~!@#$%^&*()_+-={}[];:,.<>?")

"""
