import inspect
from abc import *
from typing import overload


class ValueObject(ABC):
    __name: str
    __value: int

    @property
    def name(self) -> str:
        return self.__name

    @property
    def value(self) -> int:
        return self.__value

    def __init__(self, param) -> None:
        self.__dic = {}

        # region create and check __dic
        for name, value in inspect.getmembers(self, lambda x: type(x) == int):
            if not name.startswith('_') and name.isupper():
                self.__dic[name] = value
        self.__check_members__()
        # endregion

        self.set(param)

    # region def set
    @overload
    def set(self, val: str) -> None:
        ...

    @overload
    def set(self, val: int) -> None:
        ...

    def set(self, val) -> None:
        if type(val) is int:
            self.__name = self.get_by_value(val)
            self.__value = val
        elif type(val) is str:
            _ = self.__dic.get(val)
            if _ is None:
                raise ValueError()
            self.__name = val
            self.__value = _
        elif type(val) is type(self):
            self.set(int(self))
        else:
            raise TypeError()

    # endregion

    def get_by_value(self, value: int) -> str:
        for item, val in self.__dic.items():
            if val == value:
                return item
        raise ValueError()

    def get_by_name(self, name: str) -> int:
        if self.__dic.get(name) is None:
            raise ValueError()
        return self.__dic[name]

    def __check_members__(self):
        values = list(self.__dic.values())
        while values.__len__()>0:
            val = values.pop(0)
            if val in values:
                raise ValueError(f"duplicate value in __dic: {val} \n dic: {self.__dic}")

    def __eq__(self, other):
        if type(self) is type(other):
            return self.__value == other.value
        elif type(other) is int or type(other) is str:
            my_type = type(self)
            other_val = my_type(other)
            self.__eq__(other_val)
        return False

    def __int__(self):
        return self.__value

    def __str__(self):
        return self.__name

    def __copy__(self):
        _ = type(self)
        return _(int(self))
