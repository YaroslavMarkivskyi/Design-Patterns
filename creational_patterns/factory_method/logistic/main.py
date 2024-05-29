"""
Client code that shows realized factory method.
"""
import random

from creational_patterns.factory_method.logistic\
    .factories.truck_factory import TruckCreator
from creational_patterns.factory_method.logistic\
    .factories.plane_factory import PlaneCreator
from creational_patterns.factory_method.logistic\
    .factories.ship_factory import ShipCreator


if __name__ == "__main__":
    truck_creator = TruckCreator()
    ship_creator = ShipCreator()
    plane_creator = PlaneCreator()
    delivers = []
    for _ in range(20):
        path = random.randint(500, 1000)
        delivers.append(truck_creator.create_deliver(path=path))
        delivers.append(ship_creator.create_deliver(path=path))
        delivers.append(plane_creator.create_deliver(path=path))

    for deliver in delivers:
        time = deliver.delivery()
        print(
            "Path: " + str(deliver) +
            " delivery time: " + str(time) + " hours."
        )
