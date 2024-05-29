"""
Class that create a bus object.
"""
from .factory import CarCreator

from creational_patterns.factory_method.car_service.cars.bus import Bus
from creational_patterns.factory_method.car_service\
    .cars.car_type import CarType


class BusCreator(CarCreator):
    def create_car(self, owner: str = ''):
        car = Bus(
            owner=owner,
            type_car=CarType.bus.value
        )
        return car
