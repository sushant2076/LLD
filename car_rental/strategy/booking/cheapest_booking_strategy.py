from typing import List, Optional

from examples.car_rental.enums.pricing_strategy_type import PricingStrategyType
from examples.car_rental.model.vehicle import Vehicle
from examples.car_rental.strategy.booking.booking_strategy import BookingStrategy


class CheapestBookingStrategy(BookingStrategy):
    def __init__(self, pricing_type: PricingStrategyType):
        self.pricing_type = pricing_type

    def book_vehicle(self, vehicles: List[Vehicle]) -> Optional[Vehicle]:
        def price_key(vehicle: Vehicle) -> float:
            if self.pricing_type == PricingStrategyType.TIME_BASED:
                return vehicle.price_per_hour
            return vehicle.price_per_km

        sorted_vehicles = sorted(vehicles, key=price_key)

        for vehicle in sorted_vehicles:
            if vehicle.is_booked.compare_and_set(False, True):
                return vehicle
        return None
