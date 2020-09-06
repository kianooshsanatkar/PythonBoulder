from configuration import db
from core.domain.baseentity import Entity
from infra.datahandler import objectmodels as models
from infra.domain.entities.area import Location, Area
from infra.domain.entities.group import Group
from infra.domain.entities.person import Person, Contact
from infra.domain.entities.user import User
from infra.domain.valueobject import Permission


class ObjectModelTranslator:

    @staticmethod
    def user_translator(user: models.User, password=False) -> User:
        return User(id=user.Id, user_name=user.UserName,
                    password=user.Password if password is True else None,
                    email=user.Email,
                    mobile_number=user.MobileNumber, state=user.State, email_verified=user.EmailVerified,
                    mobile_verified=user.MobileVerified,
                    persons=[ObjectModelTranslator.person_translator(person) for person in user.Persons])

    @staticmethod
    def permissions_translator(person: models.Person):
        if person.permissions is not None and person.permissions.__len__() > 0:
            return_obj = []
            for permission in person.permissions:
                return_obj.append(Permission(permission.Permission))
            return return_obj
        return None

    @staticmethod
    def person_translator(person: models.Person, with_permission=False) -> Person:
        return Person(id=person.Id,
                      first_name=person.FirstName,
                      last_name=person.LastName,
                      birth_date=person.BirthDate,
                      gender=person.Gender,
                      permissions=None if with_permission is not True else ObjectModelTranslator.permissions_translator(
                          person),
                      user=None)

    @staticmethod
    def contact_translator(person: models.Person) -> Contact:
        return Contact(id=person.Id,
                       email=person.Email,
                       instagram=person.Instagram,
                       twitter=person.Twitter,
                       facebook=person.Facebook,
                       linkedin=person.Linkedin,
                       telegram=person.Telegram,
                       resident_location=person.ResidentLocationId)

    @staticmethod
    def group_member_translator(group: models.Group) -> [Person]:
        if group.Members is not None and group.Members.__len__() > 0:
            members = []
            for member in group.Members:
                members.append(Person(
                    id=member.Person.Id,
                    user=None,
                    first_name=member.Person.FirstName,
                    last_name=member.Person.LastName,
                    birth_date=None,
                    gender=None))
            return members

        return None

    @staticmethod
    def group_translator(group: models.Group) -> Group:
        return Group(id=group.Id,
                     title=group.Title,
                     creator=group.Creator,
                     members=ObjectModelTranslator.group_member_translator(group))

    @staticmethod
    def location_translator(location: models.Location) -> Location:
        return Location(id=location.Id,
                        lat=location.Latitude,
                        lng=Location.longitude)

    @staticmethod
    def area_translator(location: models.Location) -> Area:
        return Area(id=location.Id,
                    latitude=location.Latitude,
                    longitude=location.Longitude,
                    name=location.Name,
                    district_number=location.DistrictNumber,
                    neighborhood_name=location.NeighborhoodName,
                    full_add=location.FullAdd)

    @staticmethod
    def translate(obj: db.Base, *arguments) -> Entity:
        if isinstance(obj, models.User):
            return ObjectModelTranslator.user_translator(obj)
        # elif isinstance(obj,models.Permission):
        #     return permissions_translator(obj)
        elif isinstance(obj, models.Person):
            return ObjectModelTranslator.person_translator(obj, *arguments)
        elif isinstance(obj, models.Group):
            return ObjectModelTranslator.group_translator(obj)
        elif isinstance(obj, models.Location):
            return ObjectModelTranslator.area_translator(obj)
        else:
            raise TypeError('input variable type is not a db.Base instance')
