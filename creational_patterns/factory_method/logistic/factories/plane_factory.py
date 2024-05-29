"""
Class that creates plane deliver.
"""
from .factory import LogisticCreator
from creational_patterns.factory_method.logistic\
    .transports.plane import Plane


class PlaneCreator(LogisticCreator):
    def create_deliver(self, path: int = 0):
        transport = Plane(path=path)
        return transport
