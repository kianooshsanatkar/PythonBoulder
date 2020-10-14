import datetime
import random
from unittest import TestCase

from sqlalchemy import create_engine

from configuration import db
from core.conventions.valueobjects import Gender
from infra.datahandler.repository import InfraRepository
from infra.infrainterface import CommandsCaller, QueryCaller


class TestDbConfig(db):
    connection_str = "postgresql://IUEPA_Test:pass1234@localhost/IUEPA_Test_DB"
    create = True
    auto_commit = True


class BaseInfraFunctionalTest(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        db.echo = False

    def setUp(self) -> None:
        self.drop_tables()
        self.commands = CommandsCaller(InfraRepository(TestDbConfig.connection_str, True, True), None)
        self.queries = QueryCaller(InfraRepository(TestDbConfig.connection_str, True), None)

    def tearDown(self) -> None:
        self.drop_tables()

    def logout(self):
        self.commands.set_user(None)
        self.queries.set_user(None)

    def set_self_user(self):
        user_dict = {
            'user_name': 'sample',
            'password': 'Passw0rd',
            'email': 'sample@test.com',
            'mobile_number': '09121234567'
        }
        self.commands.register_user(user_dict)
        user = self.queries.query_user_login(user_dict['user_name'], user_dict['password'])
        self.commands.set_user(user)
        self.queries.set_user(user)
        user_dict['user'] = user
        return user_dict

    def set_self_user_Person(self):
        user_dict = self.set_self_user()
        user = user_dict['user']
        person = {
            'first_name': 'user 1',
            'last_name': 'user last_name1',
            'birth_date': datetime.date(1988, 8, 17),
            'gender': Gender.MALE,
            'user': user
        }
        person_id = self.commands.register_person(**person)
        # person = self.queries.get_person(person_id)
        # self.commands.__user__.persons.append(person)
        # self.assertTrue(self.commands.__user__.persons == self.queries.__user__.persons)
        self.logout()
        user = self.queries.query_user_login(user_dict['user_name'], user_dict['password'])
        self.commands.set_user(user)
        self.queries.set_user(user)
        return self.commands.__user__

    def create_user(self, username, email=None, password='Passw0rd'):
        if not email:
            email = f'sample{random.randint(0, 100000)}@test.com'
        user_dict = {
            'user_name': username,
            'password': password,
            'email': email
        }
        user_id = self.commands.create_blank_user(user_dict)
        user = self.queries.get_user(user_id)
        return user

    def create_user_person(self, username=None, email=None, person=None):
        if not username:
            username = f'username{random.randint(0, 100000)}'
        user = self.create_user(username, email)
        if not person:
            person = {
                'first_name': 'user 1',
                'last_name': 'user last_name1',
                'birth_date': datetime.date(1988, 8, 17),
                'gender': Gender.MALE,
                'user': user
            }
        person_id = self.commands.register_person_for(**person)

        persons = self.queries.get_person(person_id)
        return persons

    def drop_tables(self):
        engine = create_engine(TestDbConfig.connection_str)
        TestDbConfig.Base.metadata.drop_all(bind=engine)
