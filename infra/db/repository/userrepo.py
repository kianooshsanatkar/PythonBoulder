from bson import ObjectId

from infra.domain.entities.user import User, UserState
from infra.db.datamodel.usermodel import UserModel
from infra.domain.entities.Registration import RegistrationInfo
from infra.domain.entities.authentication import AuthInfo


class UserRepository:

    def __init__(self):
        pass

    def get_user(self, uid) -> User:
        u = UserModel.objects.get(id=ObjectId(uid))
        return User(u.id, u.UserName, UserState(u.UserState))

    def initiate_user(self, user: AuthInfo):
        u = UserModel(UserName=user.user_name, Password=user.password, UserState=user.state.value)
        u.save()
        return u.id

    def register_user(self, registration_info: RegistrationInfo):
        u = UserModel.objects.get(id=ObjectId(registration_info.uid))
        u.Email = str(registration_info.email)
        u.CellPhone = str(registration_info.cellphone)
        u.save()
        return u.id
