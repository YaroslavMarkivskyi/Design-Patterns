"""
Interface factory method.
"""
from abc import ABC, abstractmethod


class CarCreator(ABC):
    @abstractmethod
    def create_car(self, owner: str = ''):
        """Method that return a car."""
        pass
