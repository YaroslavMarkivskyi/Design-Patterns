"""
Class that create a truck object.
"""
from .factory import CarCreator

from creational_patterns.factory_method.car_service.cars.truck import Truck
from ..cars.car_type import CarType


class TruckCreator(CarCreator):
    def create_car(self, owner: str = ''):
        car = Truck(
            owner=owner,
            type_car=CarType.truck.value
        )
        return car
