

from enums.vehicle import VehicleType


class Vehicle:
    def __init__(self, id: str, type: VehicleType):
        self.id = id
        self.type = type