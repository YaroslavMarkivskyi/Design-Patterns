"""
Client code that creates different type of house object.
"""
from creational_patterns.builder.housing_dev.directors import HouseDirector
from creational_patterns.builder.housing_dev.builders import (
    Builder,
    HouseBuilder,
    DocsBuilder
)


def print_results(message: str, builder: Builder):
    print(f"||||| Director builds {message} house |||||")
    print(builder.product)


def use_director(builder: Builder) -> None:
    """Method that executes director's job."""
    director = HouseDirector()
    director.builder = builder

    director.build_eco_house()
    print_results("eco", builder)

    director.build_standard_house()
    print_results("standard", builder)

    director.build_premium_house()
    print_results("premium", builder)

    director.build_luxury_house()
    print_results("luxury", builder)


if __name__ == "__main__":
    house_builder = HouseBuilder()
    docs_builder = DocsBuilder()

    print("\n###Use director that builds houses####\n")
    use_director(house_builder)

    print("\n###Use director that creates documentation about houses###\n")
    use_director(docs_builder)
