"""
Interface that describes abstract factory to create products by:
apple;
samsung;
sony.
"""
from abc import ABC, abstractmethod


class ProductFactory(ABC):
    @abstractmethod
    def create_smartphone(self):
        pass

    @abstractmethod
    def create_tv(self):
        pass

    @abstractmethod
    def create_laptop(self):
        pass
