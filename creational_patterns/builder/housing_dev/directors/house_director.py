"""
CLass director that creates different house object.
"""
from ..builders import (
    Builder,
)


class HouseDirector:

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        """
        The Director works with any builder instance that
        the client code passes to it. This way,
        the client code may alter the final type of the newly
        assembled product.
        """
        self._builder = builder

    def build_eco_house(self):
        self._builder.produce_basis()
        self._builder.produce_floor()
        self._builder.produce_roof()

    def build_standard_house(self):
        self._builder.produce_basis()
        self._builder.produce_floor()
        self._builder.produce_garage()
        self._builder.produce_roof()

    def build_premium_house(self):
        self._builder.produce_basis()
        self._builder.produce_floor()
        self._builder.produce_floor()
        self._builder.produce_balcony()
        self._builder.produce_floor()
        self._builder.produce_garage()
        self._builder.produce_roof()

    def build_luxury_house(self):
        self._builder.produce_basis()
        self._builder.produce_floor()
        self._builder.produce_terrace()
        self._builder.produce_floor()
        self._builder.produce_balcony()
        self._builder.produce_floor()
        self._builder.produce_floor()
        self._builder.produce_balcony()
        self._builder.produce_floor()
        self._builder.produce_balcony()
        self._builder.produce_garage()
        self._builder.produce_roof()
