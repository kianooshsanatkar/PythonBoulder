class InternalException(Exception):
    pass


class AuthenticationException(InternalException):
    pass


class ValidationException(InternalException):
    pass


class AuthorizationException(InternalException):
    pass


class DataBaseException(InternalException):
    pass


class ValueException(ValueError):
    pass
