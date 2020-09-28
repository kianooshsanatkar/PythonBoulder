from sqlalchemy.orm import Session

from configuration import db
from core.domain.baseentity import Entity
from db.repo.absrepo import AbsRepository


# def replace_object_model_fields(base_obj: db.Base, destination_obj: db.Base):
#     __forbidden_types__ = [list, tuple, dict, set, InstrumentedList, InstrumentedDict, InstrumentedSet]
#     base_fields = inspect.getmembers(base_obj.__class__, lambda x: isinstance(x, InstrumentedAttribute))
#     for name, val in base_fields:
#         if name in base_obj.__dict__ and name in destination_obj.__dict__:
#             value = getattr(base_obj, name)
#             if type(value) not in __forbidden_types__:
#                 setattr(destination_obj, name, value)


# todo : Unit Test And Functional Test !!!
class Repository(AbsRepository):
    __type_translator_dict__: dict

    def __init__(self, session: Session):
        self.session = session

    def get_counterpart_type(self, _type: type):
        if issubclass(_type, Entity):
            if self.__type_translator_dict__ is None or self.__type_translator_dict__.__len__() < 1:
                raise NotImplementedError("'Type Translator Dictionary' is not implemented")
            return self.__type_translator_dict__[_type.__name__]
        raise TypeError('the argument type must be sub class of Entity')

    # @abstractmethod
    def get(self, uid):
        pass

    # def get_by_id(self, entity_type, entity_id) -> db.Base:
    #     return self.session.query(entity_type).get(entity_id)

    # def get(self, entity) -> db.Base:
    #     if isinstance(entity, Entity):
    #         return self.get_by_id(self.get_counterpart_type(entity.__class__), entity.uid)
    #     return self.get_by_id(entity.__class__, entity.uid)

    def add(self, entity: db.Base) -> None:
        self.session.add(entity)

    def add_range(self, entities: list) -> None:
        self.session.add_all(entities)

    # def update(self, entity: db.Base) -> None:
    #     obj = self.get(entity)
    #     replace_object_model_fields(entity, obj)
    #     self.add(obj)

    def remove(self, entity: db.Base) -> None:
        self.session.delete(entity)

    def remove_range(self, entities):
        pass

    def get_all(self, start, count):
        pass

    def find(self):
        pass

    def find_all(self):
        pass
