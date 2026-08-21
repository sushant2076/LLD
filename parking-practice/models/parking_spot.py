import threading

from enums.vehicle import Vehicle, VehicleType


class ParkingSpot:
    def __init__(self, id: str, type: VehicleType):
        self.id = id
        self.type = type
        self.is_available = True
        self._lock = threading.Lock
        
    def occupy(self):
        if self.is_available:
            self.is_available = False

            