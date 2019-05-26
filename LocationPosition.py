class LocationPosition:
    latitude: float = 0
    longitude: float = 0

    def __init__(self, latitude: float, longitude: float):
        self.latitude = latitude
        self.longitude = longitude

    def get_location(self):
        return f'{self.latitude},{self.longitude}'

    def to_json(self):
        return {
            'latitude': self.latitude,
            'longitude': self.longitude
        }
