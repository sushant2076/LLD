from collections import defaultdict
from typing import Dict, List

from examples.car_rental.enums.vehicle_type import VehicleType
from examples.car_rental.model.vehicle import Vehicle


class Branch:
    def __init__(self, id: str, city: str):
        self.id = id
        self.city = city
        self.vehicles: Dict[VehicleType, List[Vehicle]] = defaultdict(list)

    def get_vehicles_by_type(self, vehicle_type: VehicleType) -> List[Vehicle]:
        return list(self.vehicles.get(vehicle_type, []))

    def add_vehicle(self, vehicle: Vehicle) -> None:
        self.vehicles[vehicle.type].append(vehicle)

    def remove_vehicle(self, vehicle: Vehicle) -> None:
        vehicle_list = self.vehicles.get(vehicle.type)
        if vehicle_list is not None and vehicle in vehicle_list:
            vehicle_list.remove(vehicle)
