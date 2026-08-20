from __future__ import annotations
import math
from datetime import datetime, time, timedelta

from ...enums.vehicle_type import VehicleType
from .pricing_strategy import PricingStrategy

# Peak period hours (e.g., 8:00 to 17:00).
PEAK_START = time(8, 0)
PEAK_END = time(17, 0)

PEAK_RATES: dict[VehicleType, float] = {
    VehicleType.CAR: 30.0,
    VehicleType.BIKE: 15.0,
    VehicleType.TRUCK: 50.0,
}

NON_PEAK_RATES: dict[VehicleType, float] = {
    VehicleType.CAR: 20.0,
    VehicleType.BIKE: 10.0,
    VehicleType.TRUCK: 30.0,
}


def _is_peak(t: time) -> bool:
    return PEAK_START <= t <= PEAK_END


class TimeBasedPricing(PricingStrategy):
    def calculate_fee(self, vehicle_type: VehicleType, entry_time: datetime, exit_time: datetime) -> float:
        if exit_time < entry_time:
            raise ValueError("Exit time before entry time")

        duration_minutes = (exit_time - entry_time).total_seconds() / 60
        total_hours = math.ceil(duration_minutes / 60.0)

        # Count peak hours and non-peak hours by iterating hour by hour.
        peak_hours = 0
        non_peak_hours = 0

        cursor = entry_time.replace(minute=0, second=0, microsecond=0)
        # If entry time has minutes, the first hour is considered partially
        # occupied, still counted as 1 hour (already rounded above).
        for _ in range(total_hours):
            if _is_peak(cursor.time()):
                peak_hours += 1
            else:
                non_peak_hours += 1
            cursor += timedelta(hours=1)

        peak_rate = PEAK_RATES[vehicle_type]
        non_peak_rate = NON_PEAK_RATES[vehicle_type]

        return peak_hours * peak_rate + non_peak_hours * non_peak_rate
