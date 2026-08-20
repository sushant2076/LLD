from datetime import datetime

from examples.car_rental.model.vehicle import Vehicle
from examples.car_rental.strategy.pricing.pricing_strategy import PricingStrategy


class DistanceBasedPricingStrategy(PricingStrategy):
    def calculate_price(self, vehicle: Vehicle, start: datetime, end: datetime, distance_km: float) -> float:
        return distance_km * vehicle.price_per_km
