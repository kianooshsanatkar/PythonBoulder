from copy import copy
from typing import overload
from uuid import UUID

from infra.db.repository.uow import UnitOfWork
from infra.domain.entities.person import Person
from infra.domain.entities.user import User
from infra.handler.commands.personcommand import RegisterPerson, RegisterPersonFor
from infra.handler.commands.usercommand import ChangePassword, ChangeUserName, ChangeUserEmail, InitializeUser
from infra.handler.query.personquery import GetPerson, GetPersonsOfUser
from infra.handler.query.userquery import UserLogin, GetUser, GetUserPerson


class BaseCaller:

    def __init__(self, db_context, user=None):
        self.__uow__ = lambda: UnitOfWork(**db_context)
        self.__user = user

    def set_user(self, user: User):
        self.__user = user

    @property
    def __user__(self) -> User:
        return copy(self.__user)

    @property
    def prop(self):
        return {'user': self.__user__, 'uow': self.__uow__, 'adapter': self.__adapter__}


class CommandsCaller(BaseCaller):

    def __init__(self, db_context, user, adapter):
        super().__init__(db_context, user)
        self.__adapter__ = adapter

    def register_user(self, user):
        print(self.prop)
        return InitializeUser(**self.prop).execute(**user)

    def change_user_email(self, email):
        return ChangeUserEmail(**self.prop).execute(email)

    def change_username(self, username):
        return ChangeUserName(**self.prop).execute(username)

    def change_password(self, old_pass, new_pass):
        return ChangePassword(**self.prop).execute(old_pass, new_pass)

    def register_person(self, **person):
        person = Person(**person)
        return RegisterPerson(**self.prop).execute(person)

    def register_person_for(self, **person):
        person = Person(**person)
        return RegisterPersonFor(**self.prop).execute(person)


class QueryCaller(BaseCaller):

    def __init__(self, db_context, user, adapter):
        super().__init__(db_context, user)
        self.__adapter__ = adapter

    def query_user_login(self, username, password) -> User:
        return UserLogin(**self.prop).execute(username, password)

    # region get_user() Overload
    @overload
    def get_user(self, user_name: str) -> User:
        pass

    @overload
    def get_user(self, email: str) -> User:
        pass

    @overload
    def get_user(self, user_id: UUID) -> User:
        pass

    def get_user(self, discriminator) -> User:
        return GetUser(**self.prop).execute(discriminator)

    # endregion

    def get_user_person(self, discriminator) -> User:
        return GetUserPerson(**self.prop).execute(discriminator)

    def get_person(self, person_id) -> [Person]:
        return GetPerson(**self.prop).execute(person_id)

    def get_persons_of_user(self, user_id=None) -> [Person]:
        if not user_id:
            user_id = self.__user__.uid
        return GetPersonsOfUser(**self.prop).execute(user_id)
