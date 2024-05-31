"""
Client code that uses abstract factory.
"""
from creational_patterns.abstract_factory.technology_products\
    .factories import (
        ProductFactory,
        SamsungFactory,
        AppleFactory,
        SonyFactory,
    )
from creational_patterns.abstract_factory.technology_products\
    .products.base import (
        Smartphone,
        Tv,
        Laptop,
    )


def create_products(factory: ProductFactory):
    """Method that return list of products by brand."""
    laptop = factory.create_laptop()
    tv = factory.create_tv()
    smartphone = factory.create_smartphone()
    return smartphone, tv, laptop


def use_products(
        smartphone: Smartphone,
        tv: Tv,
        laptop: Laptop):
    """Method to use all products methods."""
    print("\n::::::::::Smartphone::::::::::\n")
    smartphone.turn_on()
    smartphone.call()
    smartphone.turn_off()

    print("\n::::::::::TV::::::::::::::::::\n")
    tv.turn_on()
    tv.connect_youtube()
    tv.turn_off()

    print("\n::::::::::Laptop::::::::::::::\n")
    laptop.turn_on()
    laptop.show_display()
    laptop.turn_off()


def show_result(brand: str = '', products=None):
    if products is None:
        products = []
    print(f"\n||||| ->Use product by {brand} <-|||||\n")
    use_products(*products)


if __name__ == "__main__":
    apple_products = create_products(AppleFactory())
    sony_products = create_products(SonyFactory())
    samsung_products = create_products(SamsungFactory())

    show_result("Sony", sony_products)
    show_result("Apple", apple_products)
    show_result("Samsung", samsung_products)
