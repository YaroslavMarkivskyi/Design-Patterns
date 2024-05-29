"""
Base class that describes type of cars.
"""
from abc import abstractmethod, ABC

from creational_patterns.factory_method.car_service\
    .cars.car_type import CarType


class Car(ABC):
    def __init__(self, owner: str = '', type_car: CarType = ""):
        self._type: str = type_car
        self._owner: str = owner
        self._speed: int = 0

    @abstractmethod
    def drive(self) -> None:
        """method to start engine """
        pass

    def __str__(self):
        return (
            "Type: " + self._type + '\n'
            + "Speed: " + str(self._speed) + '\n'
            + "Owner" + self._owner + '\n'
        )
