from infra.datahandler.objectmodels import Person
from infra.query.infrabasequery import InfraBaseQuery


class GetPerson(InfraBaseQuery):
    def run(self, person_id):
        with self.__data_handler__ as repo:
            person = repo.get(Person(id=person_id))
            person = self.__model_translator__.person_translator(person)
        return person

class GetPersonsOfUser(InfraBaseQuery):
    def run(self, user_id):
        with self.__data_handler__ as repo:
            persons = repo.session.query(Person).filter_by(UserId=user_id)
            persons = [self.__model_translator__.person_translator(person) for person in persons]
        return persons