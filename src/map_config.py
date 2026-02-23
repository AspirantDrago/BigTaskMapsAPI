from src.config import Config


class Map:
    MIN_SCALE = 0.000125

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

    @scale.setter
    def scale(self, scale: float) -> None:
        if scale < self.MIN_SCALE:
            return
        if ((self._latitude + scale / 2) >= 90) or ((self._latitude - scale / 2) <= -90):
            return
        self._scale = scale

    def zome_up(self) -> None:
        self.scale /= Config.SCALE_FACTOR

    def zome_down(self) -> None:
        self.scale *= Config.SCALE_FACTOR

    # def move_left(self) -> None:
    #     self.longitude -= self.scale
    #
    # def move_right(self) -> None:
    #     self.longitude += self.scale
    #
    # def move_up(self) -> None:
    #     self.latitude += self.scale
    #
    # def move_down(self) -> None:
    #     self.latitude -= self.scale