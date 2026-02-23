from src.config import Config


class Map:
    MIN_SCALE = 0.000125
    LIMIT_LATITUDE = 85

    def __init__(self, longitude: float, latitude: float, scale: float):
        self._longitude: float = longitude
        self._latitude: float = latitude
        self._scale: float = scale
        self.updated: bool = True

    @property
    def longitude(self) -> float:
        return self._longitude

    @longitude.setter
    def longitude(self, longitude: float) -> None:
        if longitude >= 180:
            longitude -= 360
        elif longitude <= -180:
            longitude += 360
        self._longitude = longitude
        self.updated = True

    @property
    def latitude(self) -> float:
        return self._latitude

    @latitude.setter
    def latitude(self, latitude: float) -> None:
        if latitude + self._scale / 2 >= self.LIMIT_LATITUDE:
            return
        if latitude - self._scale / 2 <= -self.LIMIT_LATITUDE:
            return
        self._latitude = latitude
        self.updated = True

    @property
    def scale(self) -> float:
        return self._scale

    @scale.setter
    def scale(self, scale: float) -> None:
        if scale < self.MIN_SCALE:
            return
        if (((self._latitude + scale / 2) >= self.LIMIT_LATITUDE)
                or ((self._latitude - scale / 2) <= -self.LIMIT_LATITUDE)):
            return
        self._scale = scale
        self.updated = True

    def zome_up(self) -> None:
        self.scale /= Config.SCALE_FACTOR

    def zome_down(self) -> None:
        self.scale *= Config.SCALE_FACTOR

    def move_left(self) -> None:
        self.longitude -= self.scale * Config.MOVE_FACTOR

    def move_right(self) -> None:
        self.longitude += self.scale * Config.MOVE_FACTOR

    def move_up(self) -> None:
        self.latitude += self.scale * Config.MOVE_FACTOR

    def move_down(self) -> None:
        self.latitude -= self.scale * Config.MOVE_FACTOR
