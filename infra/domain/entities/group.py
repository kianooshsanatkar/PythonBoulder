from core.domain.baseentity import Entity
from infra.domain.entities.person import Person


class Group(Entity):
    title: str
    creator: Person
    members: [Person]

    # TODO: Validation

    # def validator(self):
    #     if self.title and self.title.__len__() > 2:
    #         if self.creator and self.creator.id is not None:
    #             if self.members and self.members.__len__() > 1:
    #                 return True
    #     raise ValidationException('Group is not valid!')

    def __init__(self, uid=None, title=None, creator=None, members=None):
        super().__init__(uid)
        self.title = title
        self.creator = creator
        self.members = members
