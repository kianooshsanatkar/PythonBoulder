from sqlalchemy import Column, String, Boolean, Date, SmallInteger, ForeignKey, Integer, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, backref

from configuration import db
from core.datahandler.baseobjectmodel import BaseObjectModel


class User(BaseObjectModel, db.Base):
    __tablename__ = 'User'
    UserName = Column(String(15), unique=True, nullable=False)
    Password = Column(String(255), nullable=False)
    State = Column(Integer, nullable=False)
    Email = Column(String(255), unique=True)
    EmailVerified = Column(Boolean(), default=False, nullable=False)
    MobileNumber = Column(String(15))
    MobileVerified = Column(Boolean(), default=False, nullable=False)
    Persons = relationship('Person', backref=backref('PersonUser'))
    DateJoined = Column(Date())
    LastLogin = Column(Date())
    CurrentPersonId = Column(UUID(as_uuid=True), ForeignKey('User.Id'))

    # TODO: research on sqlalchemy if available CurrentPerson relationship
    # CurrentPerson = relationship('Person', backref=backref('CurrentPerson'))

    def __init__(self, id=None, username=None, password=None, state=None, email=None, email_verified=None, mobile=None,
                 mobile_verified=None, date_joined=None, last_login=None, persons=None):
        super().__init__(id)
        if persons is None:
            persons = []
        self.UserName = username
        self.Password = password
        self.State = state
        self.Email = email
        self.EmailVerified = email_verified
        self.MobileNumber = mobile
        self.MobileVerified = mobile_verified
        self.Persons = persons
        self.DateJoined = date_joined
        self.LastLogin = last_login


class Person(BaseObjectModel, db.Base):
    __tablename__ = 'Person'
    FirstName = Column(String(100))
    LastName = Column(String(100))
    BirthDate = Column(Date())
    Gender = Column(SmallInteger())
    UserId = Column(UUID(as_uuid=True), ForeignKey('User.Id'))
    User = relationship('User', backref=backref('UserPerson', order_by=User.Id))
    permissions = relationship('Permission', backref=backref('PermissionPerson'))
    Email = Column(String(320))
    EmailVerified = Column(Boolean())
    Instagram = Column(String(100))
    InstagramVerified = Column(Boolean())
    Twitter = Column(String(100))
    TwitterVerified = Column(Boolean())
    Facebook = Column(String(100))
    FacebookVerified = Column(Boolean())
    Linkedin = Column(String(100))
    LinkedinVerified = Column(Boolean())
    Telegram = Column(String(100))
    TelegramVerified = Column(Boolean())
    ResidentLocationId = Column(UUID(as_uuid=True), ForeignKey('Location.Id'))

    def __init__(self, id=None, firstname=None, lastname=None, birthdate=None, gender=None, userid=None,
                 email=None, emailverified=None, instagram=None, instagramverified=None, twitter=None,
                 twitterverified=None, facebook=None, facebookverified=None, linkedin=None, linkedinverified=None,
                 telegram=None, telegramverified=None, residentlocationid=None, permissions=None, user=None):
        super().__init__(id)
        if permissions is None:
            permissions = []
        self.FirstName = firstname
        self.LastName = lastname
        self.BirthDate = birthdate
        self.Gender = gender
        self.UserId = userid
        self.User = user
        self.permissions = permissions
        self.Email = email
        self.EmailVerified = emailverified
        self.Instagram = instagram
        self.InstagramVerified = instagramverified
        self.Twitter = twitter
        self.TwitterVerified = twitterverified
        self.Facebook = facebook
        self.FacebookVerified = facebookverified
        self.Linkedin = linkedin
        self.LinkedinVerified = linkedinverified
        self.Telegram = telegram
        self.TelegramVerified = telegramverified
        self.ResidentLocationId = residentlocationid


class Permission(db.Base):
    __tablename__ = 'Permission'
    PersonId = Column(UUID(as_uuid=True), ForeignKey('Person.Id'), primary_key=True)
    Permission = Column(Integer, primary_key=True)

    def __init__(self, person_id, permission):
        self.PersonId = person_id
        self.Permission = permission


class Location(BaseObjectModel, db.Base):
    __tablename__ = 'Location'
    Latitude = Column(Float())
    Longitude = Column(Float())
    Name = Column(String(50))
    Radius = Column(Float())
    DistrictNumber = Column(SmallInteger())
    NeighborhoodName = Column(String(100))
    FullAdd = Column(String(300))

    def __init__(self, id=None, latitude=None, longitude=None, name=None, radius=None, districtnumber=None,
                 neighborhoodname=None, fulladd=None):
        super().__init__(id)
        self.Latitude = latitude
        self.Longitude = longitude
        self.Name = name
        self.Radius = radius
        self.DistrictNumber = districtnumber
        self.NeighborhoodName = neighborhoodname
        self.FullAdd = fulladd


class Group(BaseObjectModel, db.Base):
    __tablename__ = 'Group'
    Creator = Column(UUID(as_uuid=True), ForeignKey('Person.Id'))
    Title = Column(String(100))
    Members = relationship('GroupMember', backref=backref('Group'))

    def __init__(self, id=None, creator=None, name=None, members=None):
        super().__init__(id)
        if members is None:
            members = []
        self.Creator = creator
        self.Title = name
        self.Members = members


class GroupMember(db.Base):
    __tablename__ = 'GroupMember'
    GroupId = Column(UUID(as_uuid=True), ForeignKey('Group.Id'), primary_key=True)
    PersonId = Column(UUID(as_uuid=True), ForeignKey('Person.Id'), primary_key=True)
    Person = relationship('Person', backref=backref('GroupMember'))

    def __init__(self, group_id=None, person_id=None, person=None):
        self.GroupId = group_id
        self.PersonId = person_id
        self.Person = person
