"""
Class that creates plane deliver.
"""
from .factory import LogisticCreator
from creational_patterns.factory_method.logistic\
    .transports.truck import Truck


class TruckCreator(LogisticCreator):
    def create_deliver(self, path: int = 0):
        transport = Truck(path=path)
        return transport
