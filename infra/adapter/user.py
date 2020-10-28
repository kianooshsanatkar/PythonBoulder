import uuid
from infra.domain.entities.user import UserState

from infra.db.datamodel.usermodel import UserModel
from infra.domain.entities.authentication import AuthInfo


def auth2user(user_auth: AuthInfo) -> UserModel:
    return UserModel(UserName=user_auth.username, Password=user_auth.password, UserState=user_auth.state.value)


def user2auth(user: UserModel) -> AuthInfo:
    return AuthInfo(uid=user.id, username=user.UserName, state=UserState(user.UserState), password=user.Password)
