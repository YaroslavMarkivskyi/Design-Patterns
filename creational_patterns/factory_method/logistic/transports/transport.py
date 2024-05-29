"""
Interface to describe delivery transports.
"""
from abc import ABC, abstractmethod


class Transport(ABC):
    def __init__(self, path: int = 0):
        self._path = path

    @abstractmethod
    def delivery(self):
        pass
