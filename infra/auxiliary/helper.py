import re

from passlib.hash import pbkdf2_sha256


def hashing_string(string: str) -> str:
    return pbkdf2_sha256.hash(string)


def is_hashed(string: str) -> bool:
    return pbkdf2_sha256.identify(string)


def hash_match(hashed: str, string: str):
    return pbkdf2_sha256.verify(string, hashed)


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
