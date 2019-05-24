class LocationPosition:
    __latitude__: float = 0
    __longitude__: float = 0

    def __init__(self, latitude, longitude):
        self.__latitude__ = latitude
        self.__longitude__ = longitude

    def get_location(self):
        return f'{self.__latitude__},{self.__longitude__}'
