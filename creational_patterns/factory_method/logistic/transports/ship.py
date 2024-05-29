"""
Class to describe delivery by ship.
"""
from .transport import Transport
from .speed_enum import SpeedEnum


class Ship(Transport):
    def delivery(self) -> float:
        time = round(self._path / SpeedEnum.ship_speed.value, 2)
        return time
