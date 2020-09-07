from core.exceptionhandler.exceptions import AuthenticationException
from infra.handler.commands.infrabasecommand import InfraBaseCommand
from infra.domain.entities.user import User
from infra.domain.valueobject import UserState
from infra.resource import ResourceManager, Texts
from infra.datahandler import objectmodels as model


class RegisterUser(InfraBaseCommand):

    def authorize(self):
        return True

    def run(self, user: User):
        if self.current_user is not None:
            raise AuthenticationException(
                ResourceManager.translate(Texts.ALREADY_LOGGED_IN)
            )
        user.state = UserState.REGISTERED
        user.validation()
        user_model = self.__entity_translator__.user_translator(user)
        with self.__data_handler__ as repo:
            repo.insert(user_model)
            return user_model.uid


class CreateBlankUser(InfraBaseCommand):

    def authorize(self):
        return True

    def run(self, user: User):
        user.state = UserState.REGISTERED
        user.validation()
        user_model = self.__entity_translator__.user_translator(user)
        with self.__data_handler__ as repo:
            repo.insert(user_model)
            return user_model.uid


class ChangeUserEmail(InfraBaseCommand):

    def run(self, new_email):
        user = self.current_user
        user.email = new_email
        user.email_validation()
        with self.__data_handler__ as repo:
            user_model = repo.get(user)
            user_model.Email = user.email
            repo.insert(user_model)
        # todo: Send EmailVerification Code


class ChangeUserName(InfraBaseCommand):

    def run(self, new_user_name):
        user = self.current_user
        user.user_name = new_user_name
        user.__username_validation()
        with self.__data_handler__ as repo:
            user_model = repo.get(user)
            user_model.UserName = user.user_name
            repo.insert(user_model)


class ChangePassword(InfraBaseCommand):

    def run(self, old_pass, new_pass):
        with self.__data_handler__ as repo:
            user_model = repo.get(model.User(self.current_user.uid))
            user = self.__model_translator__.user_translator(user_model, True)
            user.password_verification(old_pass)
            user.password_validation(new_pass)
            user.set_new_password(new_pass)
            user_model.Password = user.password
            repo.insert(user_model)
