from core.exceptionhandler.exceptions import ValidationException
from infra.handler.commands.infrabasecommand import InfraBaseCommand
from infra.domain.entities.person import Person
from infra.datahandler import objectmodels as model


class RegisterPerson(InfraBaseCommand):
    def run(self, person:Person):
        person_model = self.__entity_translator__.person_translator(person, None, None)
        with self.__data_handler__ as repo:
            user = repo.get(self.current_user)
            person_model.User = user
            person_model.UserId = user.uid
            repo.insert(person_model)
            return person_model.uid

class RegisterPersonFor(InfraBaseCommand):

    def authorize(self) -> bool:
        # TODO: check the right permission
        return super().authorize()

    def run(self, person:Person):
        if not person.user or not person.user.uid:
            raise ValidationException('user is missing!')
        person_model = self.__entity_translator__.person_translator(person, None, None)
        with self.__data_handler__ as repo:
            user = repo.get_by_id(model.User, person.user.uid)
            person_model.User = user
            person_model.UserId = user.uid
            repo.insert(person_model)
            return person_model.uid
