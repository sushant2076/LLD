from typing import List, Optional

from car_rental.model.vehicle import Vehicle
from car_rental.strategy.booking.booking_strategy import BookingStrategy


class LeastBookedVehicleStrategy(BookingStrategy):
    def book_vehicle(self, vehicles: List[Vehicle]) -> Optional[Vehicle]:
        sorted_vehicles = sorted(vehicles, key=lambda v: v.booking_count)

        for vehicle in sorted_vehicles:
            # Attempt to atomically set is_booked from False to True
            if vehicle.is_booked.compare_and_set(False, True):
                # Successfully booked
                return vehicle
            # else, this vehicle is already booked, try next

        # No vehicle could be booked
        return None
