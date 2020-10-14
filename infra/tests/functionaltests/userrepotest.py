from unittest import TestCase

from infra.db.datamodel.usermodel import UserModel
from infra.db.repository.uow import UnitOfWork
from infra.domain.entities.authentication import AuthInfo
from infra.domain.entities.user import UserState


class UserRepositoryTest(TestCase):

    def test_initiate_user(self):
        with UnitOfWork('EF_User_Test', 'User') as uow:
            UserModel.drop_collection()
            user = AuthInfo(user_name="UserTest", state=UserState.INITIALIZED, password='test_pass')
            uid = uow.user_repository.initiate_user(user)
            print(type(uid))
            user_in_db = uow.user_repository.get_user(uid)

            self.assertEqual(user.user_name, user_in_db.user_name)
            self.assertEqual(user.state, user_in_db.state)
