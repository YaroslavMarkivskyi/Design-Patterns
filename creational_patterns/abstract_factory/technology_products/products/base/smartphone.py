"""
Base class that describes smartphone functionality.
"""
from abc import ABC, abstractmethod


class Smartphone(ABC):
    @abstractmethod
    def call(self):
        pass

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass
