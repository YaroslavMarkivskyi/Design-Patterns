"""
Class that creates sony products.
"""
from .product_factory import ProductFactory
from ..products.sony import (
    SonyLaptop,
    SonySmartphone,
    SonyTv,
)


class SonyFactory(ProductFactory):
    def create_smartphone(self):
        return SonySmartphone()

    def create_tv(self):
        return SonyTv()

    def create_laptop(self):
        return SonyLaptop()
