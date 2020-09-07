from datetime import date

from core.domain.baseentity import Entity
from core.domain.helper import Gender
from infra.domain.entities.area import Location
from infra.domain.entities.user import User
from infra.domain.valueobject import Permission


class Person(Entity):
    user: User
    permissions: [Permission]
    first_name: str
    last_name: str
    birth_date: date
    gender: Gender

    def __init__(self, uid=None, first_name=None, last_name=None, birth_date=None, gender=None, permissions=None,
                 user=None):
        super().__init__(uid)
        self.user = user
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.gender = gender
        self.permissions = permissions


class Contact(Entity):
    email: str
    email_verified: bool
    instagram: str
    twitter: str
    facebook: str
    linkedin: str
    telegram: str
    resident_location: Location

    def __init__(self, uid, email, instagram, twitter, facebook, linkedin, telegram, resident_location):
        super().__init__(uid)
        self.email = email
        self.email_verified = email
        self.instagram = instagram
        self.twitter = twitter
        self.facebook = facebook
        self.linkedin = linkedin
        self.telegram = telegram
        self.resident_location = resident_location
