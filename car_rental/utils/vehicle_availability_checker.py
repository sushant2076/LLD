from datetime import datetime
from typing import List

from examples.car_rental.enums.booking_status import BookingStatus
from examples.car_rental.model.booking import Booking


class VehicleAvailabilityChecker:
    @staticmethod
    def is_available(bookings: List[Booking], start: datetime, end: datetime) -> bool:
        active_bookings = sorted(
            (b for b in bookings if b.status in (BookingStatus.CREATED, BookingStatus.CONFIRMED)),
            key=lambda b: b.start_time,
        )

        for b in active_bookings:
            existing_start = b.start_time
            existing_end = b.end_time

            overlaps = not (end < existing_start or start > existing_end)
            if overlaps:
                return False
        return True
