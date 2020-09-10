from auxiliary.helper import is_number


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


class Location:
    latitude: float
    longitude: float

    def __init__(self, uid=None, lat: float = None, lng: float = None):
        super().__init__(uid)
        if not is_number(lat) or not is_number(lng):
            raise ValueError("location must have both parameters lat and lng")

        self.latitude = lat
        self.longitude = lng


class URL:

    def __eq__(self, o: object) -> bool:
        raise NotImplementedError()

    def __str__(self) -> str:
        raise NotImplementedError()

    def read(self, number: str):
        raise NotImplementedError()

    pass


class SocialMediaAccount:
    def __eq__(self, o: object) -> bool:
        raise NotImplementedError()

    def __str__(self) -> str:
        raise NotImplementedError()

    def read(self, number: str):
        raise NotImplementedError()

    pass
