from uuid import UUID

from bson import ObjectId

from infra.db.datamodel.usermodel import UserModel


class UserRepository:

    def __init__(self):
        pass

    @staticmethod
    def get_user(uid) -> UserModel:
        return UserModel.objects.get(id=ObjectId(uid))

    @staticmethod
    def get_by_username(username: str) -> UserModel:
        return UserModel.objects(UserName__exact=username.lower()).first()

    @staticmethod
    def initiate_user(user: UserModel) -> UUID:
        user.save()
        return user.id

    @staticmethod
    def register_user(registration_info) -> UUID:
        u = UserModel.objects.get(id=ObjectId(registration_info.uid))
        u.Email = str(registration_info.email)
        u.CellPhone = str(registration_info.cellphone)
        u.save()
        return u.id
