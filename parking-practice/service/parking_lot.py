import datetime
import threading
from time import clock_settime
from typing import Optional
import uuid

from models.parking_floor import ParkingFloor
from models.ticket import Ticket
from models.vehicle import Vehicle


class ParkingLot:
    _instance: Optional["ParkingLot"] = None
    _lock = threading.Lock
    
    def __init__(self, pricing_strategy):
        self.pricing_strategy = pricing_strategy
        self.floors: dict[str, ParkingFloor] = []
    
    @classmethod
    def get_instance(cls) -> "ParkingLot":
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = cls()
        return cls._instance
    
    def park(self, vehicle: Vehicle):
        for floor_id, floor in self.floors.items():
            spot = floor.find_free_spot(vehicle)
            if spot:
                ticket = Ticket(id=uuid, entry_time=datetime, vehicle=vehicle, parking_spot=spot)
                print(f"Ticket issued")
        
        print(f"No ticket issued")
        return None
    
    def unpark(self, ticket: Ticket):
        pass
        