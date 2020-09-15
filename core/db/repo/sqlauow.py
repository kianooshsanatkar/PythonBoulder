from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from configuration import db
from core.db.repo.iuow import IUnitOfWork


class UnitOfWork(IUnitOfWork):
    __AUTO_COMMIT__ = False
    __rollback__ = False
    __session__ = None

# Todo: Transaction Implementation

    def __init__(self, url=None, create=False, auto_commit=False):
        self.__AUTO_COMMIT__ = auto_commit
        # super().__init__(context)
        self.engine = create_engine(db.connection_str, echo=db.echo) if url is None else \
            create_engine(url, echo=db.echo)
        if create is True:
            db.Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.connect()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.__rollback__ is True:
            self.__session__.rollback()
        elif self.__AUTO_COMMIT__ is True:
            self.__session__.commit()
        self.close()

    def connect(self):
        self.__session__ = self.Session()

    def close(self):
        self.__session__.close()

    def commit(self):
        self.__session__.commit()
        self.__rollback__ = False

    def rollback(self) -> None:
        self.__session__.rollback()
        self.__rollback__ = False

    # def commit(self) -> None:
    #     self.session.commit()
    #     self.__rollback = False
