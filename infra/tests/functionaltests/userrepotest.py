# todo: delete this test (create unittest with mocking for UOW)
# from unittest import TestCase
#
# from infra.domain.services.authservice import create_user_auth
# from infra.db.datamodel.usermodel import UserModel
# from infra.db.repository.uow import UnitOfWork
# from infra.domain.entities.user import UserState
#
#
# class UserRepositoryTest(TestCase):
#
#     def test_initiate_user(self):
#         with UnitOfWork('EF_User_Test', 'User') as uow:
#             UserModel.drop_collection()
#             user = create_user_auth(username="UserTest", state=UserState.INITIALIZED, password='test_pass')
#             uid = uow.user_repository.initiate_user(user)
#             print(type(uid))
#             user_in_db = uow.user_repository.get_user(uid)
#
#             self.assertEqual(user.username, user_in_db.username)
#             self.assertEqual(user.state, user_in_db.state)
