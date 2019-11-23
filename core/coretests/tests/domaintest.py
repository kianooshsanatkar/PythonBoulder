import inspect
from unittest import TestCase
from core.domain.basevalueobject import ValueObject


class TestValueObject(TestCase):
    # region helper functions
    class IncorrectValueType(ValueObject):
        VAR1 = 1
        VAR2 = 2
        VAR3 = 1

    class CorrectValueType(ValueObject):
        VAR1 = 1
        VAR2 = 2

    class CorrectValueType2(ValueObject):
        VAR1 = 1
        VAR2 = 2

    class SecondChild(CorrectValueType):
        VAR3 = 3
        VAR4 = 4
        VAR5 = 5

    # endregion

    # check members duplicate value
    def test_fail_to_create(self):
        self.assertRaises(ValueError, lambda: self.IncorrectValueType(self.IncorrectValueType.VAR1))

    def test_equal_fail(self):
        vo = self.CorrectValueType(self.CorrectValueType.VAR2)
        vo2 = self.CorrectValueType2(self.CorrectValueType2.VAR2)

        self.assertFalse("VAR2" == vo)
        self.assertFalse(vo == "VAR2")
        self.assertFalse(vo.__eq__("VAR2"))
        self.assertFalse(vo2.__eq__(vo))

        self.assertFalse(2 == vo)
        self.assertFalse(vo.__eq__(2))
        self.assertFalse(vo2.__eq__(vo))

        '''there is a defect in value object code, when we equal string or int with value objects and it's 
        result is  true cause in int or string __eq__ it doesn't check type and cast class to int or
        string so result is true!'''
        # self.assertFalse((2).__eq__(correct))
        # self.assertFalse("VAR2".__eq__(correct))

    def test_create_equal_true(self):
        vo = self.CorrectValueType(self.CorrectValueType.VAR2)
        correct2 = self.CorrectValueType(self.CorrectValueType.VAR2)

        '''value-int check'''
        self.assertEqual(self.CorrectValueType.VAR2, vo.value)
        self.assertEqual(self.CorrectValueType.VAR2, int(vo))

        '''name-str check'''
        self.assertEqual("VAR2", vo.name)
        self.assertEqual("VAR2", str(vo))

        '''obj-obj check'''
        self.assertTrue(correct2.__eq__(vo))
        self.assertTrue(correct2.__eq__(vo))

    def test_set(self):
        def by_int():
            vo = self.CorrectValueType(self.CorrectValueType.VAR2)
            vo.set(1)
            self.assertEqual(1, int(vo))
            self.assertEqual('VAR1', str(vo))

        def by_str():
            vo = self.CorrectValueType(self.CorrectValueType.VAR2)
            vo.set('VAR1')
            self.assertEqual(1, int(vo))
            self.assertEqual('VAR1', str(vo))

        by_int()
        by_str()

    def test_copy(self):
        vo = self.CorrectValueType(self.CorrectValueType.VAR2)
        ref_vo = vo
        vo.set(1)

        self.assertEqual(vo, ref_vo)
        self.assertTrue(vo == ref_vo)
        self.assertTrue(vo.__eq__(ref_vo))

        vo = self.CorrectValueType(self.CorrectValueType.VAR2)
        vo2 = vo.__copy__()
        vo.set(1)
        self.assertNotEqual(vo, vo2)
        self.assertTrue(vo != vo2)
        self.assertFalse(vo == vo2)
        self.assertFalse(vo.__eq__(vo2))

    def test_member_of_dic(self):
        vo = self.CorrectValueType(self.CorrectValueType.VAR2)
        for x, y in inspect.getmembers(vo):
            if "_ValueObject__dic" in x:
                self.assertEqual(y, {'VAR1': 1, 'VAR2': 2})

    def test_child_of_child(self):
        vo = self.SecondChild(self.SecondChild.VAR3)
        for x, y in inspect.getmembers(vo):
            if "_ValueObject__dic" in x:
                self.assertEqual(y, {'VAR1': 1, 'VAR2': 2, 'VAR3': 3, 'VAR4': 4, 'VAR5': 5})


#todo: TestEntity
# class TestEntity(TestCase):
#     pass
