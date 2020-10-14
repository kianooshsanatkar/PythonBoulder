from core.db.mongoenginerepo.mongouow import BaseUnitOfWork
from infra.db.repository.userrepo import UserRepository


class UnitOfWork(BaseUnitOfWork):

    def __init__(self, db=None, alias=None, host=None, port=None):
        super().__init__(db, alias, host, port)
        self.user_repository = UserRepository()

    def commit(self):
        pass
