from core.exceptionhandler.exceptions import AuthenticationException
from infra.datahandler import objectmodels as model
from infra.db.datamodel.usermodel import UserModel
from infra.domain.entities.user import User, UserState
from infra.domain.services.authservice import create_user_auth
from infra.handler.commands.infrabasecommand import InfraBaseCommand
from infra.resource import ResourceManager, Texts


class InitializeUser(InfraBaseCommand):

    def authorize(self) -> bool:
        return True

    def run(self, *args, **kwargs):
        if self.current_user is not None:
            raise AuthenticationException(
                ResourceManager.translate(Texts.ALREADY_LOGGED_IN)
            )
        user_model = self.adp(create_user_auth(kwargs['username'], UserState.INITIALIZED, kwargs['password']))
        # Todo: MongoDb DataHandler Implementation
        with self.__uow__() as uow:
            return uow.user_repository.insert_user(user_model)


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
        user.username = new_user_name
        user.username()
        with self.__data_handler__ as repo:
            user_model = repo.get(user)
            user_model.UserName = user.username
            repo.insert(user_model)


class ChangePassword(InfraBaseCommand):

    def run(self, old_pass, new_pass):
        with self.__data_handler__ as repo:
            user_model = repo.get(model.User(self.current_user.uid))
            user = self.__model_translator__.user_translator(user_model, True)
            user.password_verification(old_pass)
            user.password_validation(new_pass)
            user.new_password(new_pass)
            user_model.Password = user.password
            repo.insert(user_model)
