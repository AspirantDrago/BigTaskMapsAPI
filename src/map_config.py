class Map:
    def __init__(self, longitude: float, latitude: float, scale: float):
        self._longitude: float = longitude
        self._latitude: float = latitude
        self._scale: float = scale

    @property
    def longitude(self) -> float:
        return self._longitude

    @property
    def latitude(self) -> float:
        return self._latitude

    @property
    def scale(self) -> float:
        return self._scale
