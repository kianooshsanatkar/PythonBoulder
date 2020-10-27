from core.conventions.conventionalobjects import Email, CellPhone
from infra.domain.entities.user import User


class RegistrationInfo(User):

    def __init__(self, uid=None, username=None, state=None, email: Email = None,
                 cellphone: CellPhone = None, persons=None, current_person=None):
        super().__init__(uid, username, state)
        self.cellphone = cellphone
        self.email = email
        self.persons = persons
        self.current_person = current_person
