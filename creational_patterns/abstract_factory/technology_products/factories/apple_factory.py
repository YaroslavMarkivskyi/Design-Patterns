"""
Class that creates apple products.
"""
from .product_factory import ProductFactory
from ..products.apple import (
    AppleLaptop,
    AppleSmartphone,
    AppleTv,
)


class AppleFactory(ProductFactory):
    def create_smartphone(self):
        return AppleSmartphone()

    def create_tv(self):
        return AppleTv()

    def create_laptop(self):
        return AppleLaptop()
