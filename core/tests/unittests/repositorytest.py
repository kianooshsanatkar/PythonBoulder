from unittest import TestCase
from uuid import uuid4

from sqlalchemy import Column, String, Integer

from configuration import db
from datahandler.baseobjectmodel import BaseObjectModel
from db.repo.sqlarepo import Repository
from db.repo.sqlauow import UnitOfWork


class TestDataModel(BaseObjectModel, db.Base):
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
    def __init__(self):
        super().__init__(create=True)
        # super(TestUOW, self).__init__()
        self.test_repo = TestDataRepo(self.__session__, create=True)


class RepositoryTest(TestCase):

    def test_add(self):
        with TestUOW() as uow:
            uid = uuid4()
            obj = TestDataModel(name="Test2", state=3, Id=uid)
            uow.test_repo.add(obj)
            uow.commit()
            ts_obj = uow.test_repo.get(uid)
            print(ts_obj.Name)
        print("it is done")
