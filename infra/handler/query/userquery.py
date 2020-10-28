from uuid import UUID

import bson

from core.auxiliary.helper import is_UUID
from core.exceptionhandler.exceptions import AuthenticationException, ValidationException
from infra.domain.entities.authentication import AuthInfo
from infra.datahandler import objectmodels as model
from infra.domain.services.authservice import password_verification
from infra.domain.validation import password_validation
from infra.handler.query.infrabasequery import InfraBaseQuery
from infra.resource import ResourceManager, Texts


class UserLogin(InfraBaseQuery):

    def authorize(self) -> bool:
        return True

    def run(self, username: str, password: str):

        # <editor-fold desc="Check if password is valid and if user already logged-in">
        try:
            password_validation(password)
            # todo: instead of raising error we can log-out the user
            if self.current_user is not None:
                raise AuthenticationException('User is already Logged-in!')
        except Exception as er:
            raise AuthenticationException(ResourceManager.translate(Texts.LOGIN_VALUE_INCORRECT))
        # </editor-fold>

        # todo: detect if it's email or username
        # todo: implement find by email

        with self.__uow__() as uow:
            user = self.adp(uow.user_repository.get_by_username(username), AuthInfo)
            password_verification(auth=user, password=password)
            return user


class GetUser(InfraBaseQuery):
    def authorize(self) -> bool:
        return True

    def run(self, discriminator):
        with self.__uow__() as uow:
            if isinstance(discriminator, bson.ObjectId):
                return self.adp(uow.user_repository.get_user(discriminator), AuthInfo)
            elif isinstance(discriminator, str):
                return self.adp(uow.user_repository.get_by_username(discriminator), AuthInfo)
            else:
                raise ValidationException('Discriminator is not valid!')


# TODO: Guess DOn't User Ever
class GetUserPerson(InfraBaseQuery):
    def run(self, discriminator):
        with self.__data_handler__ as repo:
            if isinstance(discriminator, UUID) or is_UUID(discriminator):
                user = repo.get_by_id(model.User, discriminator)
            elif isinstance(discriminator, str):
                user = repo.get_user_by_username(discriminator)
                if user is None:
                    user = repo.get_user_by_Email(discriminator)
                else:
                    raise ValidationException(f'input value for discriminator is not valid = {discriminator}')
            if user:
                user_entity = self.__model_translator__.user_translator(user)

                person_entity = None
                if user.Persons:
                    person_entity = [self.__model_translator__.person_translator(person) for person in user.Persons]
                    if user.Persons.__len__() == 1:
                        user_entity.__current_person__ = self.__model_translator__.person_translator(user.Persons[0])
                    elif user.Persons.__len__() > 1 and user.CurrentPersonId:
                        current_person = user.Persons.find(Id=user.CurrentPersonId)
                        user_entity.__current_person__ = self.__model_translator__.person_translator(current_person)

                return user_entity, person_entity
        return None
