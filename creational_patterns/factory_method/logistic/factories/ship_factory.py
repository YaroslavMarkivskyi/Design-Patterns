"""
Class that creates plane deliver.
"""
from .factory import LogisticCreator
from creational_patterns.factory_method.logistic\
    .transports.ship import Ship


class ShipCreator(LogisticCreator):
    def create_deliver(self, path: int = 0):
        transport = Ship(path=path)
        return transport
