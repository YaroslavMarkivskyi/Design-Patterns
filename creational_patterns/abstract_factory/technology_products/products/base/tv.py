"""
Base class that describes tv functionality.
"""
from abc import ABC, abstractmethod


class Tv(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def connect_youtube(self):
        pass
