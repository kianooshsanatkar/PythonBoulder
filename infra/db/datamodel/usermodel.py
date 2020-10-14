from mongoengine import *


class UserModel(Document):
    # regex=r"^[a-z0-9]+[_a-z0-9]*[a-z0-9]+$",
    UserName = StringField(unique=True, required=True, min_length=4,
                           max_length=30)
    Password = StringField(required=True)
    UserState = IntField(required=True)
    Email = StringField(null=True, max_length=250, unique=True, sparse=True)
    IsEmailVerified = BooleanField(default=False, required=True)
    CellPhone = StringField(null=True, max_length=20, unique=True, sparse=True)
    IsCellPhoneVerified = BooleanField(default=False, required=True)



