from core.auxiliary.helper import is_number
from core.domain.baseentity import Entity


class Location(Entity):

    def __init__(self, id=None, lat: float = None, lng: float = None):
        super().__init__(id)
        if not is_number(lat) or not is_number(lng):
            raise ValueError("location must have both parameters lat and lng")

        self.latitude = lat
        self.longitude = lng

    latitude: float
    longitude: float


class Area(Location):
    name: str
    # location: Location
    radius: float
    district_number: int
    neighborhood_name: str
    full_add: str

    def __init__(self, id=None, latitude=None, longitude=None, name=None, district_number=None,
                 neighborhood_name=None, full_add=None):
        super().__init__(id, latitude, longitude)
        self.name = name
        # self.location = location
        self.district_number = district_number
        self.neighborhood_name = neighborhood_name
        self.full_add = full_add
