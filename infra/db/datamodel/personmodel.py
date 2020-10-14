from mongoengine import *


class PersonModel:
    FirstName = StringField()
    MiddleName = StringField()
    LastName = StringField()
    DisplayName = StringField()
    Birth = DateField()
    IdentityId = StringField()
    Gender = DateField()
