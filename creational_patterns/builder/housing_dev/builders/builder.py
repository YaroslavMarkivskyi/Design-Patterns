"""
 The Builder interface specifies methods for creating the different parts of
 the House objects.
"""
from abc import ABC, abstractmethod


class Builder(ABC):
    @property
    @abstractmethod
    def product(self):
        pass

    @abstractmethod
    def produce_basis(self):
        pass

    @abstractmethod
    def produce_floor(self):
        pass

    @abstractmethod
    def produce_balcony(self):
        pass

    @abstractmethod
    def produce_roof(self):
        pass

    @abstractmethod
    def produce_terrace(self):
        pass

    @abstractmethod
    def produce_garage(self):
        pass
