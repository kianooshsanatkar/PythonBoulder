from core.domain.basevalueobject import ValueObject


# todo: class Responsibility(ValueObject):
class Responsibility(ValueObject):
    pass


class UserState(ValueObject):
    REGISTERED = 1
    ACTIVE = 2
    SUSPEND = 3
    DEACTIVATE = 4


class Permission(ValueObject):
    SYSTEM = 0
    ACTIVE = 100
    AID = 200
    SOCIAL_NETWORK = 300
    MAIL_SERVICE = 400
