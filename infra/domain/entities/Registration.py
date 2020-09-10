from core.domain.ConventionalObjects import Email, CellPhone
from infra.domain.entities.user import User
from infra.domain.valueobject import UserState


class RegistrationInfo(User):

    def __init__(self, uid=None, user_name=None, state=UserState.DEACTIVATE, email: Email = None,
                 cellphone: CellPhone = None, persons=None, current_person=None):
        super().__init__(uid, user_name, state)
        self.cellphone = cellphone
        self.email = email
        self.persons = persons
        self.current_person = current_person