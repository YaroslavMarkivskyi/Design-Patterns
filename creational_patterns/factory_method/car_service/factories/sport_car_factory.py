"""
Class that create a sport-car object.
"""
from .factory import CarCreator

from creational_patterns.factory_method.car_service\
    .cars.sport_car import SportCar
from ..cars.car_type import CarType


class SportCarCreator(CarCreator):
    def create_car(self, owner: str = ''):
        car = SportCar(
            owner=owner,
            type_car=CarType.sport_car.value
        )
        return car
