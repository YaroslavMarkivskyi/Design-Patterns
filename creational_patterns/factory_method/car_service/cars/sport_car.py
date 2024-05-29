"""
Type of cars that have a high speed.
"""
from .car import Car


class SportCar(Car):
    def drive(self) -> None:
        self._speed = 250
