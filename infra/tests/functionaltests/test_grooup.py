# Todo: Delete
# Group Entity is deleted

"""

from infra.tests.functionaltests.basefunctional import BaseInfraFunctionalTest


class GroupTest(BaseInfraFunctionalTest):

    def test_group_insert(self):
        assert 1 == 1
        self.set_self_user_Person()

        # user = self.set_self_user()
        person1 = self.create_user_person()
        person2 = self.create_user_person()
        person3 = self.create_user_person()
        person4 = self.create_user_person()
        group_id = self.commands.create_new_group('my group', [person1.uid, person2.uid, person3.uid, person4.uid])
        group = self.queries.get_group_by_id(group_id)
        group_by_title = self.queries.get_group_by_title('my group')
        self.assertIsNotNone(group)
        self.assertIsNotNone(group_by_title)
        self.assertTrue(4 == group.members.__len__() == group_by_title.members.__len__())
        self.assertTrue('my group' == group.title == group_by_title.title)

"""
