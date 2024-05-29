"""
Truck class that has a low speed.
"""
from .car import Car


class Truck(Car):
    def drive(self) -> None:
        self._speed = 75
