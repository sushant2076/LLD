from __future__ import annotations
import math
from datetime import datetime

from ...enums.vehicle_type import VehicleType
from .pricing_strategy import PricingStrategy

# Event pricing: higher per-hour rates.
EVENT_HOURLY_RATES: dict[VehicleType, float] = {
    VehicleType.CAR: 50.0,
    VehicleType.BIKE: 30.0,
    VehicleType.TRUCK: 70.0,
}


class EventBasedPricing(PricingStrategy):
    def calculate_fee(self, vehicle_type: VehicleType, entry_time: datetime, exit_time: datetime) -> float:
        duration_minutes = (exit_time - entry_time).total_seconds() / 60
        hours = math.ceil(duration_minutes / 60.0)  # always round up to next hour

        rate_per_hour = EVENT_HOURLY_RATES.get(vehicle_type, 0.0)
        return rate_per_hour * hours
