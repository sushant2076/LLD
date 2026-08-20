from ..enums.vehicle_type import VehicleType
from ..model.bike import Bike
from ..model.car import Car
from ..model.truck import Truck
from ..model.vehicle import Vehicle

_CREATORS = {
    VehicleType.CAR: Car,
    VehicleType.BIKE: Bike,
    VehicleType.TRUCK: Truck,
}


class VehicleFactory:
    """Mirrors VehicleFactory.java."""

    @staticmethod
    def create(number: str, vehicle_type: VehicleType) -> Vehicle:
        try:
            cls = _CREATORS[vehicle_type]
        except KeyError as exc:
            raise ValueError(f"Unsupported vehicle type: {vehicle_type}") from exc
        return cls(number)
