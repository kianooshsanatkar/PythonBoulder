class Email:
    def __eq__(self, o: object) -> bool:
        raise NotImplementedError()

    def __str__(self) -> str:
        raise NotImplementedError()


class CellPhone:
    def __eq__(self, o: object) -> bool:
        raise NotImplementedError()

    def __str__(self) -> str:
        raise NotImplementedError()

    def read(self, number: str):
        raise NotImplementedError()

    pass
