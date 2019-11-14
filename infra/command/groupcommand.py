from infra.command.infrabasecommand import InfraBaseCommand
from infra.datahandler import objectmodels as model
from infra.domain.entities.group import Group
from infra.domain.entities.person import Person


class CreateNewGroup(InfraBaseCommand):
    def run(self, group: Group):
        group_model = model.Group(None, self.current_user.__current_person__.id, group.title)
        with self.__data_handler__ as repo:
            repo.insert(group_model)
            repo.session.flush()
            for member in group.members:
                person = repo.get(Person(id=member.id))
                repo.insert(model.GroupMember(group_model.Id, person.Id, person))

            return group_model.Id
