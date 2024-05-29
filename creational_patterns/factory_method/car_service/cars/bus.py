"""
Bus class that has low speed.
"""
from .car import Car


class Bus(Car):
    def drive(self) -> None:
        self._speed = 50
