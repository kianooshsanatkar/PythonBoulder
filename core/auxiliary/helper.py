import re
from uuid import UUID

from passlib.hash import pbkdf2_sha256


def is_number(obj) -> bool:
    if obj is None:
        return False
    if type(obj) is int:
        return True
    if type(obj) is float:
        return True

    return False


def hashing_string(string: str) -> str:
    return pbkdf2_sha256.hash(string)


def is_hashed(string: str) -> bool:
    return pbkdf2_sha256.identify(string)


def hash_match(hashed: str, string: str):
    return pbkdf2_sha256.verify(string, hashed)


def extract_numbers(string: str, phone_first00=False) -> str:
    """
    remove everything but numbers
    :param phone_first00: bool
    :param string: string
    :return: string
    """
    regex = r"\D"
    return ("+" + re.sub(regex, "", string)) if phone_first00 is True and string[0] == "+" \
        else re.sub(regex, "", string)


def password_validation(password: str):
    if is_hashed(password):
        return True
    # regex = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[a-zA-Z\d\-_.!@#$%^&*()+=~`:;<>\?,{}[\] ]{6,31}$"
    regex = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[\d\-_\.!@#$%^&*()+=~`:;<>\?,{}[\] ])" \
            "[a-zA-Z\d\-_\.!@#$%^&*()+=~`:;<>\?,{}[\] ]{6,31}$"
    if re.match(regex, password):
        return True
    return False


def username_validation(username: str) -> bool:
    if 2 < username.__len__() < 16:
        regex = r"^[a-z0-9]+[_a-z0-9]*[a-z0-9]+$"
        if re.match(regex, username, re.IGNORECASE):
            return True
    return False


def mobile_number_validator(mobile: str) -> bool:
    regex = r"^(\+98|98|0|)9\d{9}$"
    if re.match(regex, mobile):
        return True
    return False


def email_validator(email: str) -> bool:
    if email.__len__() <= 320:
        regex = r"(^([a-z0-9]+[_.]*[a-z0-9]+)+@[a-z0-9-]{3,}\.([a-z]+\.)*[a-z]{2,}$)"
        if re.match(regex, email, re.IGNORECASE):
            return True
    return False


def is_UUID(string: str,empty_uuid=True):
    if empty_uuid:
        regex = r'^[0-9A-F]{8}-([0-9A-F]{4}-){3}[0-9A-F]{12}$'
    else:
        # this is stronger but not working for empty uuid
        regex = r'^[0-9A-F]{8}-[0-9A-F]{4}-4[0-9A-F]{3}-[89AB][0-9A-F]{3}-[0-9A-F]{12}$'

    if re.match(regex, string, re.IGNORECASE):
        return True
    return False


def get_empty_UUID():
    return UUID('00000000-0000-0000-0000-000000000000')


def is_UUID_empty(uid):
    return get_empty_UUID().__eq__(uid)

# class Email:
#     local_part: str
#     domain_name: str
#     dns_name: str
#
#     def __init__(self, email_address: str):
#         temp = email_address.split("@")
#         self.local_part = temp[0]
#         temp = temp[1]
#         self.domain_name = temp.split(".")[0]
#         self.dns_name = temp[1][temp[1].index(".") + 1:]
