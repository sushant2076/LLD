from abc import ABC, abstractmethod
from typing import List, Optional

from car_rental.model.vehicle import Vehicle


class BookingStrategy(ABC):
    @abstractmethod
    def book_vehicle(self, vehicles: List[Vehicle]) -> Optional[Vehicle]:
        raise NotImplementedError
