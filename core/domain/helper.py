from core.domain.basevalueobject import ValueObject


class FiveLevel(ValueObject):
    TRIVIAL = 1
    NORMAL = 2
    IMPORTANT = 3
    VERY_IMPORTANT = 4
    CRITICAL = 5


class ImportanceLevel(FiveLevel):
    ...


class DangerLevel(FiveLevel):
    ...


class Animal(ValueObject):
    CAT = 1
    DOG = 2
    BIRD = 3


class Gender(ValueObject):
    MALE = 1
    Female = 2
    OTHER = 3
