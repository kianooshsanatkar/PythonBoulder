from infra.datahandler import objectmodels as models
from infra.domain.entities import user, person, area, group


class EntityTranslator:

    @staticmethod
    def user_translator(entity: user.User) -> models.User:
        return models.User(id=entity.id,
                           username=entity.user_name,
                           password=entity.password,
                           state=entity.state,
                           email=entity.email,
                           email_verified=entity.email_verified,
                           mobile=entity.mobile_number,
                           mobile_verified=entity.mobile_verified)

    @staticmethod
    def person_translator(person_e: person.Person, contact_e: person.Contact = None, user_id=None) -> models.Person:
        if contact_e:
            object_model = models.Person(id=person_e.id,
                                         firstname=person_e.first_name,
                                         lastname=person_e.last_name,
                                         birthdate=person_e.birth_date,
                                         gender=person_e.gender,
                                         userid=person_e.user.id if person_e.user and person_e.user.id else user_id,
                                         email=contact_e.email,
                                         emailverified=contact_e.email_verified,
                                         instagram=contact_e.instagram,
                                         instagramverified=None,
                                         twitter=contact_e.twitter,
                                         twitterverified=None,
                                         facebook=contact_e.facebook,
                                         facebookverified=None,
                                         linkedin=contact_e.linkedin,
                                         linkedinverified=None,
                                         telegram=contact_e.telegram,
                                         telegramverified=None,
                                         residentlocationid=contact_e.resident_location,
                                         permissions=None,
                                         user=None)
        else:
            object_model = models.Person(id=person_e.id,
                                         firstname=person_e.first_name,
                                         lastname=person_e.last_name,
                                         birthdate=person_e.birth_date,
                                         gender=person_e.gender,
                                         userid=person_e.user.id if person_e.user and person_e.user.id else user_id,
                                         user=None)

        # if user_id is not None:
        #     object_model.UserId = str(user_id)
        # elif person_e.user is not None:
        #     object_model.UserId = str(person_e.user.id)
        # if person_e.user is not None:
        #     object_model.User = user_translator(person_e.user)

        return object_model

    @staticmethod
    def permission_translator(entity: person.Person) -> [models.Permission]:
        if entity.permissions is not None and entity.permissions.__len__() > 0:
            permissions = []
            for x in entity.permissions:
                permissions.append(models.Permission(entity.id, x.value))
            return permissions
        return None

    @staticmethod
    def location_translator(entity) -> models.Location:
        if type(entity) is area.Area:
            return models.Location(entity.id,
                                   entity.latitude,
                                   entity.longitude,
                                   entity.name,
                                   entity.radius,
                                   entity.district_number,
                                   entity.neighborhood_name,
                                   entity.full_add)
        elif type(entity) is area.Location:
            return models.Location(entity.id,
                                   entity.latitude,
                                   entity.longitude)

        raise ValueError('input type is incorrect')

    @staticmethod
    def group_members_translator(entity: group.Group) -> [models.GroupMember]:
        if entity.members is not None and entity.members.__len__() > 0:
            members = []
            for member in entity.members:
                members.append(models.GroupMember(entity.id, member.id))
            return members
        return None

    @staticmethod
    def group_translator(entity: group.Group) -> models.Group:
        return models.Group(entity.id, entity.creator.id, entity.title,
                            EntityTranslator.group_members_translator(entity))
