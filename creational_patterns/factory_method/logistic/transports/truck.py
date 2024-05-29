"""
Class to describe delivery by plane.
"""
from .transport import Transport
from .speed_enum import SpeedEnum


class Truck(Transport):
    def delivery(self) -> float:
        time = round(self._path / SpeedEnum.truck_speed.value, 2)
        return time
