"""
Builder class that creates docs about House object.
"""
from .builder import Builder
from creational_patterns.builder.housing_dev.products import House as Product


class DocsBuilder(Builder):
    def __init__(self):
        self._product = Product()
        self._floor = 0
        self.reset()

    def reset(self):
        self._product = Product()
        self._floor = 0

    @property
    def product(self) -> Product:
        product = self._product
        self.reset()
        return product

    def produce_basis(self):
        self._product.add("This house has basis")

    def produce_floor(self):
        self._floor += 1
        self._product.add(f"This house has {self._floor} floors")

    def produce_balcony(self):
        self._product.add("This house has balcony")

    def produce_roof(self):
        self._product.add("This house has roof")

    def produce_terrace(self):
        self._product.add("This house has terrace")

    def produce_garage(self):
        self._product.add("this house has garage")
