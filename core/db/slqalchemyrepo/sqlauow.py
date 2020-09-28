from sqlalchemy.orm import sessionmaker, Session

from core.db.repo.absuow import AbsUnitOfWork


class UnitOfWork(AbsUnitOfWork):

    def __init__(self, context: Session, auto_commit=False):
        super().__init__(context)
        self.__context__.autocommit = auto_commit

    def connect(self):
        pass

    def close(self):
        self.__context__.close()

    def commit(self):
        self.__context__.commit()

    def rollback(self) -> None:
        self.__context__.rollback()

