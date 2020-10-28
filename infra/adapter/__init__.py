from adapter.user import auth2user, user2auth
from infra.domain.entities.Registration import RegistrationInfo
from infra.domain.entities.authentication import AuthInfo
from infra.domain.entities.user import User


def db_model_adapter(obj):
    """
    :param obj: the object that we want to translate.
    :return: A DataBase Model object
    """

    def raise_error():
        raise NotImplementedError()

    adapter_factory = {
        AuthInfo: auth2user,
        User: raise_error,
        RegistrationInfo: raise_error
    }
    adaptable = type(obj)
    return adapter_factory[adaptable](obj)


def entity_adapter(obj, adapted_type):
    """
    :param obj: the object that we want to translate.
    :param adapted_type: the type that object must translated to.
    :return: An Entity object.
    """

    def raise_error():
        raise NotImplementedError()

    adapter_factory = {
        AuthInfo: user2auth,
        User: raise_error,
        RegistrationInfo: raise_error
    }

    return adapter_factory[adapted_type](obj)
