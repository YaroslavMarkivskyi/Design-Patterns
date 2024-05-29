"""
Client code that creates cars using factory method.
"""
from creational_patterns.factory_method.car_service\
    .factories.bus_factory import BusCreator
from creational_patterns.factory_method.car_service\
    .factories.truck_factory import TruckCreator
from creational_patterns.factory_method.car_service\
    .factories.sport_car_factory import SportCarCreator


if __name__ == "__main__":
    for i in range(1, 20):
        truck = TruckCreator().create_car(owner=f"truck_owner_{i}")
        bus = BusCreator().create_car(owner=f"bus_owner_{i}")
        sport_car = SportCarCreator().create_car(owner=f"sport_car_owner_{i}")
        print(truck)
        print(bus)
        print(sport_car)
