from core.exceptions import AuthenticationException
from infra.domain.valueobject import UserState
from infra.infratests.functionaltests.basefunctional import BaseInfraFunctionalTest


class UserTest(BaseInfraFunctionalTest):

    def test_user_register_login(self):
        user = {
            'user_name': 'test_user_name',
            'password': 'Passw0rd',
            'email': 'test@test.com',
            'mobile_number': '09121234567'
        }

        self.commands.register_user(user)
        get_user = self.queries.query_user_login(user['user_name'], user['password'])
        self.assertEqual(user['user_name'], get_user.user_name)
        self.assertEqual(user['email'], get_user.email)
        self.assertEqual(UserState.REGISTERED, get_user.state)
        self.assertEqual(user['mobile_number'], get_user.mobile_number)
        # not login when already login
        self.set_self_user()
        self.assertRaises(AuthenticationException,self.queries.query_user_login,user['user_name'], user['password'])
        #password validation Exception
        self.assertRaises(AuthenticationException,self.queries.query_user_login,user['user_name'], 'password')


    def test_login_by_email(self):
        user = self.set_self_user()
        self.assertRaises(AuthenticationException,self.queries.query_user_login,user['email'],user['password'])
        self.logout()
        get_user = self.queries.query_user_login(user['email'],user['password'])
        self.assertIsNotNone(get_user)

    def test_change_email(self):
        user = self.set_self_user()
        user['email'] = 'newemail@test.com'
        self.commands.change_user_email(user['email'])
        changed_user = self.queries.get_user(user['user_name'])
        self.assertEqual(user['email'],changed_user.email)
        changed_user = self.queries.get_user(user['email'])
        self.assertEqual(user['email'],changed_user.email)

    def test_change_username(self):
        user = self.set_self_user()
        user['user_name'] = 'new_username'
        self.commands.change_username(user['user_name'])
        changed_user = self.queries.get_user(user['email'])
        self.assertEqual(user['user_name'],changed_user.user_name)

    def test_change_password(self):
        user = self.set_self_user()
        new_pass='Pa$$w0rd'
        self.assertRaises(AuthenticationException,self.commands.change_password,'wrong_pass',new_pass)
        self.commands.change_password(user['password'],new_pass)
        self.logout()
        changed_user = self.queries.query_user_login(user['user_name'],new_pass)
        self.assertIsNotNone(changed_user)
        self.assertEqual(changed_user.user_name,user['user_name'])

    #TODO: Create Test For **Craete_Blank_User**