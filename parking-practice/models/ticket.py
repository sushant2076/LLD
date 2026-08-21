import datetime

from attr import dataclass

from models.parking_spot import ParkingSpot
from models.vehicle import Vehicle

@dataclass
class Ticket:
    id: str
    entry_time: datetime
    vehicle: Vehicle
    parking_spot: ParkingSpot
    