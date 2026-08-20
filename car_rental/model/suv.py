from examples.car_rental.enums.vehicle_type import VehicleType
from examples.car_rental.model.vehicle import Vehicle


class SUV(Vehicle):
    def __init__(self, license_plate: str, price_per_hour: float, price_per_km: float):
        super().__init__(license_plate, price_per_hour, price_per_km, VehicleType.SUV)
