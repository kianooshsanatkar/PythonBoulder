from core.datahandler.repository import GenericRepository
from infra.datahandler import objectmodels
from infra.domain.entities.area import Area, Location
from infra.domain.entities.group import Group
from infra.domain.entities.person import Person, Contact
from infra.domain.entities.user import User
from infra.domain.valueobject import Permission


class InfraRepository(GenericRepository):
    __type_translator_dict__ = {
        User.__name__: objectmodels.User,
        Person.__name__: objectmodels.Person,
        Permission.__name__: objectmodels.Permission,
        Group.__name__: objectmodels.Group,
        Area.__name__: objectmodels.Location,
        Location.__name__: objectmodels.Location,
        Contact.__name__: objectmodels.Person
    }

    def get_user_by_username(self, username: str) -> objectmodels.User:
        return self.session.query(objectmodels.User).filter_by(UserName=username).first()

    def get_user_by_Email(self, email: str) -> objectmodels.User:
        return self.session.query(objectmodels.User).filter_by(Email=email).first()
