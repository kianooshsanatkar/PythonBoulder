from copy import copy
from typing import overload
from uuid import UUID

from infra.command.groupcommand import CreateNewGroup
from infra.command.personcommand import RegisterPerson, RegisterPersonFor
from infra.command.usercommand import ChangePassword, ChangeUserName, ChangeUserEmail, RegisterUser, CreateBlankUser
from infra.datahandler.repository import InfraRepository
from infra.domain.entities.group import Group
from infra.domain.entities.person import Person
from infra.domain.entities.user import User
from infra.query.groupquery import GetGroupById, GetGroupByTitle
from infra.query.personquery import GetPerson, GetPersonsOfUser
from infra.query.userquery import UserLogin, GetUser, GetUserPerson


class BaseCaller:

    def __init__(self, repository: InfraRepository, user=None):
        self.__repo__ = repository
        self.__user = user

    def set_user(self, user: User):
        self.__user = user

    @property
    def __user__(self) -> User:
        return copy(self.__user)

    @property
    def prop(self):
        return {'user': self.__user__, 'data_handler': self.__repo__}


class CommandsCaller(BaseCaller):

    def register_user(self, user):
        if isinstance(user, dict):
            user = User(**user)
        return RegisterUser(**self.prop).execute(user)

    def create_blank_user(self, user):
        if isinstance(user, dict):
            user = User(**user)
        return CreateBlankUser(**self.prop).execute(user)

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

    def create_new_group(self, group_title: str, members: list):
        contact_members = [Person(id=member) for member in members]
        return CreateNewGroup(**self.prop).execute(Group(title=group_title, members=contact_members))


class QueryCaller(BaseCaller):

    def query_user_login(self, username, password):
        return UserLogin(**self.prop).execute(username, password)

    @overload
    def get_user(self, user_name: str):
        pass

    @overload
    def get_user(self, email: str):
        pass

    @overload
    def get_user(self, user_id: UUID):
        pass

    def get_user(self, discriminator) -> User:
        return GetUser(**self.prop).execute(discriminator)

    def get_user_person(self, discriminator) -> User:
        return GetUserPerson(**self.prop).execute(discriminator)

    def get_person(self, person_id) -> [Person]:
        return GetPerson(**self.prop).execute(person_id)

    def get_persons_of_user(self, user_id=None) -> [Person]:
        if not user_id:
            user_id = self.__user__.id
        return GetPersonsOfUser(**self.prop).execute(user_id)

    def get_group_by_id(self, group_id)->Group:
        return GetGroupById(**self.prop).execute(group_id)

    def get_group_by_title(self, group_id)->Group:
        return GetGroupByTitle(**self.prop).execute(group_id)
