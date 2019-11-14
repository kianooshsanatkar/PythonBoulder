import inspect
from abc import ABC

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.attributes import InstrumentedAttribute
from sqlalchemy.orm.collections import InstrumentedSet, InstrumentedDict, InstrumentedList

from configuration import db
from core.domain.baseentity import Entity


def replace_object_model_fields(base_obj: db.Base, destination_obj: db.Base):
    __forbidden_types__ = [list, tuple, dict, set, InstrumentedList, InstrumentedDict, InstrumentedSet]
    base_fields = inspect.getmembers(base_obj.__class__, lambda x: isinstance(x, InstrumentedAttribute))
    for name, val in base_fields:
        if name in base_obj.__dict__ and name in destination_obj.__dict__:
            value = getattr(base_obj, name)
            if type(value) not in __forbidden_types__:
                setattr(destination_obj, name, value)


# todo : Unit Test And Functional Test !!!
class GenericRepository:
    __AUTO_COMMIT__ = False
    __rollback = False
    __type_translator_dict__: dict

    def __init__(self, url=None, create=False, auto_commit=False):
        self.__AUTO_COMMIT__ = auto_commit
        self.engine = create_engine(db.connection_str, echo=db.echo) if url is None else \
            create_engine(url, echo=db.echo)
        if create is True:
            db.Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def get_counterpart_type(self, _type: type):
        if issubclass(_type, Entity):
            if self.__type_translator_dict__ is None or self.__type_translator_dict__.__len__() < 1:
                raise NotImplementedError("'Type Translator Dictionary' is not implemented")
            return self.__type_translator_dict__[_type.__name__]
        raise TypeError('the argument type must be sub class of Entity')

    def connect(self):
        self.session = self.Session()

    def close(self):
        self.session.close()

    def get_by_id(self, entity_type, entity_id) -> db.Base:
        return self.session.query(entity_type).get(entity_id)

    def get(self, entity) -> db.Base:
        if isinstance(entity, Entity):
            return self.get_by_id(self.get_counterpart_type(entity.__class__), entity.id)
        return self.get_by_id(entity.__class__, entity.Id)

    def insert(self, entity: db.Base) -> None:
        self.session.add(entity)

    def add_range(self, entities: list) -> None:
        self.session.add_all(entities)

    def update(self, entity: db.Base) -> None:
        obj = self.get(entity)
        replace_object_model_fields(entity, obj)
        self.insert(obj)

    def delete(self, entity: db.Base) -> None:
        self.session.delete(entity)

    def commit(self) -> None:
        self.session.commit()
        self.__rollback = False

    def rollback(self) -> None:
        self.session.rollback()
        self.__rollback = False

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.__rollback is True:
            self.session.rollback()
        elif self.__AUTO_COMMIT__ is True:
            self.session.commit()
        self.close()
