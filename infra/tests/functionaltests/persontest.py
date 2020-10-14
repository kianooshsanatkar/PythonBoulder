# Todo: Rewrite Test

"""
import datetime

from core.conventions.valueobjects import Gender
from infra.tests.functionaltests.basefunctional import BaseInfraFunctionalTest


class PersonTest(BaseInfraFunctionalTest):

    def test_person_create(self):
        user = self.set_self_user()
        person = {
            'first_name': 'user 1',
            'last_name': 'user last_name1',
            'birth_date': datetime.date(1988, 8, 17),
            'gender': Gender.MALE
        }
        self.commands.register_person(**person)

        persons = self.queries.get_persons_of_user()
        self.assertEqual(1, persons.__len__())
        __person = persons[0]
        self.assertEqual(person['first_name'],__person.first_name)
        self.assertEqual(person['last_name'],__person.last_name)
        self.assertEqual(person['birth_date'],__person.birth_date)
        self.assertEqual(person['gender'],__person.gender)


    #TODO: Create Test for **Register_Person_For**
"""
