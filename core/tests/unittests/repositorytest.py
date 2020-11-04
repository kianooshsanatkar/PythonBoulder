from unittest import TestCase
from uuid import uuid4

from sqlalchemy import Column, String, Integer

from core.configuration import TestDb
from core.datahandler.baseobjectmodel import BaseObjectModel
from core.db.slqalchemyrepo.sqlarepo import Repository
from core.db.slqalchemyrepo.sqlauow import UnitOfWork
from core.db.slqalchemyrepo.sqlauowmanager import UowConfiguration


class TestDataModel(BaseObjectModel, TestDb.Base):
    __tablename__ = "TestTable"

    def __init__(self, name, state, Id=None):
        super().__init__(Id)
        self.Name = name
        self.State = state

    Name = Column(String(255), nullable=False)
    State = Column(Integer, nullable=True)


class TestDataRepo(Repository):

    def get(self, uid):
        return self.session.query(TestDataModel).get(uid)


class TestUOW(UnitOfWork):
    def __init__(self, context, auto_commit=False):
        super().__init__(context, auto_commit)
        self.test_repo = TestDataRepo(self.__context__)


class RepositoryTest(TestCase):

    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.uowm = UowConfiguration(TestDb, create=True)

    def tearDown(self) -> None:
        super().tearDown()
        TestDb.Base.metadata.drop_all(bind=self.uowm.engine)

    def test_add(self):
        expected_name = "Test2"
        expected_state = 3
        uid = uuid4()
        context = self.uowm.get_context()
        with TestUOW(context) as uow:
            obj = TestDataModel(name=expected_name, state=3, Id=uid)
            uow.test_repo.add(obj)
            uow.commit()
            ts_obj = uow.test_repo.get(uid)
            self.assertEqual(expected_name, ts_obj.Name)
            self.assertEqual(expected_state, ts_obj.State)
