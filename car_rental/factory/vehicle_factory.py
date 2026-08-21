from car_rental.enums.vehicle_type import VehicleType
from car_rental.model.sedan import Sedan
from car_rental.model.suv import SUV
from car_rental.model.vehicle import Vehicle


class VehicleFactory:
    @staticmethod
    def create(vehicle_type: VehicleType, license_plate: str, price_per_hour: float, price_per_km: float) -> Vehicle:
        if vehicle_type == VehicleType.SEDAN:
            return Sedan(license_plate, price_per_hour, price_per_km)
        if vehicle_type == VehicleType.SUV:
            return SUV(license_plate, price_per_hour, price_per_km)
        raise ValueError(f"Unsupported vehicle type: {vehicle_type}")
