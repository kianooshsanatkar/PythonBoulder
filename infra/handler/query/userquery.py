from uuid import UUID

from core.auxiliary.helper import is_UUID
from core.exceptionhandler.exceptions import AuthenticationException, ValidationException
from infra.datahandler import objectmodels as model
from infra.domain.entities.user import User
from infra.handler.query.infrabasequery import InfraBaseQuery
from infra.resource import ResourceManager, Texts


class UserLogin(InfraBaseQuery):

    def authorize(self) -> bool:
        return True

    def run(self, username: str, password: str):
        try:
            User().password_validation(password)
            if self.current_user is not None:
                raise AuthenticationException()
        except:
            raise AuthenticationException(ResourceManager.translate(Texts.LOGIN_VALUE_INCORRECT))
        with self.__data_handler__ as repo:
            user_model = repo.session.query(model.User).filter_by(UserName=username).first()
            if user_model is None:
                user_model = repo.session.query(model.User).filter_by(Email=username).first()
                if user_model is None:
                    raise AuthenticationException('User didn\'t exist')
            current_person_id = user_model.CurrentPersonId
            user = self.__model_translator__.user_translator(user_model, True)

        user.password_verification(password)

        if user.persons and user.persons.__len__() > 0:
            if user.persons.__len__() == 1:
                user.__current_person__ = user.persons[0]
            elif current_person_id:
                user.__current_person__ = filter(lambda pr: pr.uid == current_person_id, user.persons).__next__()
        return User(user.uid, username, None, user.email, user.cellphone, user.state, user.email_verified,
                    user.mobile_verified,
                    None if user.__current_person__ else user.persons, user.__current_person__)


class GetUser(InfraBaseQuery):
    def run(self, discriminator):
        with self.__data_handler__ as repo:
            if isinstance(discriminator, UUID):
                user = repo.get_by_id(model.User, discriminator)
            elif isinstance(discriminator, str):
                user = repo.get_user_by_username(discriminator)
                if user is None:
                    user = repo.get_user_by_Email(discriminator)
            if user:
                user_entity = self.__model_translator__.user_translator(user)
                # if user.Persons.__len__() == 1:
                #     user_entity.__current_person__ = self.__model_translator__.person_translator(user.Persons[0])
                # elif user.Persons.__len__() > 1 and user.CurrentPersonId:
                #     current_person = user.Persons.find(Id=user.CurrentPersonId)
                #     user_entity.__current_person__ = self.__model_translator__.person_translator(current_person)
                return user_entity
        return None


#TODO: Guess DOn't User Ever
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
