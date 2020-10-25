from unittest import TestCase

from infra.auxiliary.helper import password_validation, username_validation, hashing_string, hash_match

from passlib.hash import pbkdf2_sha256


class ValidationTest(TestCase):

    def test_password_validation(self):
        self.assertTrue(password_validation("Tt3456"))
        self.assertTrue(password_validation("123ttT"))
        self.assertTrue(password_validation("As13$#"))
        self.assertTrue(password_validation("AsFd$#"))
        self.assertTrue(password_validation("AFqr1234!@#$%^&*()_+-=[]{}:;<>?"))
        self.assertFalse(password_validation("Tt345"))
        self.assertFalse(password_validation("tt3456"))
        self.assertFalse(password_validation("Tttttt"))
        self.assertFalse(password_validation("123456"))
        self.assertFalse(password_validation("Tt1234'"))
        self.assertFalse(password_validation("Tt1234\""))
        self.assertFalse(password_validation("Tt1234/"))
        self.assertFalse(password_validation("Tt1234\\"))
        self.assertFalse(password_validation("asdf!@#$%"))
        self.assertFalse(password_validation("1234%$#@"))
        self.assertFalse(password_validation("Tt1" * 10 + "32"))
        self.assertFalse(password_validation(""))

    def test_username_validation(self):
        self.assertFalse(username_validation(""))
        self.assertFalse(username_validation("t"))
        self.assertFalse(username_validation("tt"))
        self.assertFalse(username_validation("_ttt"))
        self.assertFalse(username_validation("ttt_"))
        self.assertFalse(username_validation("tt.t"))
        self.assertFalse(username_validation("tt-t"))
        self.assertFalse(username_validation("\"''][{}-0=-0/.شسیابتنب"))
        self.assertTrue(username_validation("ttt"))
        self.assertTrue(username_validation("tt_t"))
        self.assertTrue(username_validation("t_t"))
        self.assertTrue(username_validation("ttttttttttttttt"))
        self.assertTrue(username_validation("123"))
        self.assertTrue(username_validation("123"))

    def test_hashing(self):
        string = "test"
        hashed = hashing_string(string)
        self.assertNotEqual(string, hashed)
        self.assertTrue(pbkdf2_sha256.verify(string, hashed))

    def test_hash_match(self):
        string = "test"
        hashed = hashing_string(string)
        self.assertNotEqual(string, hashed)
        self.assertTrue(pbkdf2_sha256.verify(string, hashed))
        self.assertTrue(hash_match(hashed, string))
