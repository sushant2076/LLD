from models.parking_spot import ParkingSpot
from models.vehicle import Vehicle


class ParkingFloor:
    def __init__(self, id):
        self.id = id
        self.spots: dict[str, ParkingSpot] = []
        
    def add_spots(self, id, parking_spot: ParkingSpot):
        self.spots[id] = parking_spot
        
    def find_free_spot(self, vehicle: Vehicle):
        for spot_id, spot in self.spots.items():
            if spot.type is vehicle.type and spot.occupy(vehicle):
                return spot
        return None