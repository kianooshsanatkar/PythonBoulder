from datetime import date

from core.domain.baseentity import Entity
from core.conventions.conventionalobjects import Location, Email
from core.conventions.socialmediaobjects import *
from conventions.valueobjects import Gender
from infra.domain.entities.user import User


class Person(Entity):
    user: User
    # permissions: [Permission]
    first_name: str
    middle_name: str
    last_name: str
    identity_id: str
    birth_date: date
    gender: Gender

    def __init__(self, uid=None, first_name=None, last_name=None, middle_name=None, identity_id=None, birth_date=None,
                 gender=None, permissions=None, user=None):
        super().__init__(uid)
        self.identity_id = identity_id
        self.middle_name = middle_name
        self.user = user
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.gender = gender
        self.permissions = permissions


class Contact(Person):
    email: Email
    instagram: InstagramAccount
    twitter: TwitterAccount
    facebook: FacebookAccount
    linkedin: LinkedinAccount
    telegram: TelegramAccount
    resident_location: Location

    def __init__(self, uid, email, instagram, twitter, facebook, linkedin, telegram, resident_location):
        super().__init__(uid)
        self.email = email
        self.instagram = instagram
        self.twitter = twitter
        self.facebook = facebook
        self.linkedin = linkedin
        self.telegram = telegram
        self.resident_location = resident_location
