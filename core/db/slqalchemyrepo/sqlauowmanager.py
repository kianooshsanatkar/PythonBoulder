from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from core.db.repo.iuowmanager import IUnitOfWorkConfiguration


class UowConfiguration(IUnitOfWorkConfiguration):
    def __init__(self, db, url=None, create=False):
        self.engine = create_engine(db.connection_str, echo=db.echo) if url is None else \
            create_engine(url, echo=db.echo)
        if create is True:
            db.Base.metadata.create_all(self.engine)
        self.__Session__ = sessionmaker(bind=self.engine)

    def get_context(self) -> Session:
        return self.__Session__()

    # def __exit__(self, exc_type, exc_val, exc_tb):
    #     self.engine.dispose()
