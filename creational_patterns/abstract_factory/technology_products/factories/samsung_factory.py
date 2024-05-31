"""
Class that creates samsung products.
"""
from .product_factory import ProductFactory
from ..products.samsung import (
    SamsungLaptop,
    SamsungSmartphone,
    SamsungTv,
)


class SamsungFactory(ProductFactory):
    def create_smartphone(self):
        return SamsungSmartphone()

    def create_tv(self):
        return SamsungTv()

    def create_laptop(self):
        return SamsungLaptop()
