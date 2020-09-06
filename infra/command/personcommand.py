from core.exceptions import ValidationException
from infra.command.infrabasecommand import InfraBaseCommand
from infra.domain.entities.person import Person
from infra.datahandler import objectmodels as model


class RegisterPerson(InfraBaseCommand):
    def run(self, person:Person):
        person_model = self.__entity_translator__.person_translator(person, None, None)
        with self.__data_handler__ as repo:
            user = repo.get(self.current_user)
            person_model.User = user
            person_model.UserId = user.Id
            repo.insert(person_model)
            return person_model.Id

class RegisterPersonFor(InfraBaseCommand):

    def authorize(self) -> bool:
        # TODO: check the right permission
        return super().authorize()

    def run(self, person:Person):
        if not person.user or not person.user.id:
            raise ValidationException('user is missing!')
        person_model = self.__entity_translator__.person_translator(person, None, None)
        with self.__data_handler__ as repo:
            user = repo.get_by_id(model.User,person.user.id)
            person_model.User = user
            person_model.UserId = user.Id
            repo.insert(person_model)
            return person_model.Id