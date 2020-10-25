import uuid
from unittest import TestCase
from core.auxiliary.helper import *


class HelperTest(TestCase):

    def test_is_number(self):
        self.assertFalse(is_number(None))
        self.assertFalse(is_number("str"))
        self.assertFalse(is_number([]))
        self.assertFalse(is_number(()))
        self.assertFalse(is_number({}))
        self.assertFalse(is_number(int))
        self.assertFalse(is_number(float))
        self.assertTrue(is_number(1))
        self.assertTrue(is_number(1.0))

    def test_email_validator(self):
        self.assertTrue(email_validator("test.test@test.test"))
        self.assertTrue(email_validator("tt@ttt.tt"))
        self.assertTrue(email_validator("1tt1@ttt.tt"))
        self.assertTrue(email_validator("tt.tt_t@tt-t.tt"))
        self.assertTrue(email_validator("t" * 313 + "@ttt.tt"))  # total length = 320
        self.assertFalse(email_validator("t" * 314 + "@ttt.tt"))  # total length = 321
        self.assertFalse(email_validator("t@ttt.tt"))
        self.assertFalse(email_validator("tt@tt.tt"))
        self.assertFalse(email_validator("tt@ttt.t"))
        self.assertFalse(email_validator("tt@tttt..tt"))
        self.assertFalse(email_validator("tt.@ttt.tt"))
        self.assertFalse(email_validator("tt_@ttt.tt"))
        self.assertFalse(email_validator("tt@tt_t.tt"))
        self.assertFalse(email_validator("tt@ttt.t-t"))
        self.assertFalse(email_validator("tt@ttt.t_t"))
        self.assertFalse(email_validator(".tt@ttt.tt"))
        self.assertFalse(email_validator("tt@ttt.tt."))

    def test_mobile_number_validator(self):
        self.assertTrue(mobile_number_validator("9121234567"))
        self.assertTrue(mobile_number_validator("9301234567"))
        self.assertTrue(mobile_number_validator("09121234567"))
        self.assertTrue(mobile_number_validator("9121234567"))
        self.assertTrue(mobile_number_validator("+989121234567"))
        self.assertFalse(mobile_number_validator(""))
        self.assertFalse(mobile_number_validator("1"))
        self.assertFalse(mobile_number_validator("91212345678"))
        self.assertFalse(mobile_number_validator("93012345678"))
        self.assertFalse(mobile_number_validator("091212345678"))
        self.assertFalse(mobile_number_validator("+9891212345678"))
        self.assertFalse(mobile_number_validator("912123456"))
        self.assertFalse(mobile_number_validator("930123456"))
        self.assertFalse(mobile_number_validator("0912123456"))
        self.assertFalse(mobile_number_validator("+98912123456"))
        self.assertFalse(mobile_number_validator("8121234567"))
        self.assertFalse(mobile_number_validator("08121234567"))
        self.assertFalse(mobile_number_validator("+988121234567"))
        self.assertFalse(mobile_number_validator("912123456t"))
        self.assertFalse(mobile_number_validator("912-234567"))
        self.assertFalse(mobile_number_validator("912.234567"))

    def test_extract_number_in_string(self):
        string = "djdfjadwytvmn..--__  ,,یشبلسالب12345poydfghzxcqwer..--__ +_)((*&&^%%$#@! ,,فغعه" \
                 "><:L'\"\\//][}{تنلئد6789qerasdfzxcdf..--__  ],؛ـآۀـآّ،ريالآۀّ"
        expected_string = "123456789"
        self.assertEqual(expected_string, extract_numbers(string))
        expected_string2 = "+" + expected_string
        string = "+" + string
        self.assertEqual(expected_string, extract_numbers(string))
        self.assertEqual(expected_string, extract_numbers(string))
        self.assertEqual(expected_string2, extract_numbers(string, True))

    def test_isUUID_and_get_emptyUUID(self):
        self.assertEqual(True,is_UUID(str(uuid.uuid4())))
        self.assertEqual(False,is_UUID(str(uuid.uuid4())[0:-1]))
        self.assertEqual(False,is_UUID(str(uuid.uuid4())[1:]))
        self.assertEqual(True,is_UUID(str(get_empty_UUID())))
        self.assertEqual(False,is_UUID(str(get_empty_UUID()),False))
