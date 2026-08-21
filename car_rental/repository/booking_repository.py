from typing import Dict, List, Optional

from car_rental.model.booking import Booking


class BookingRepository:
    def __init__(self):
        self._bookings: Dict[str, Booking] = {}

    def add_booking(self, booking: Booking) -> None:
        self._bookings[booking.booking_id] = booking

    def get_booking_by_id(self, booking_id: str) -> Optional[Booking]:
        return self._bookings.get(booking_id)

    def remove_booking(self, booking_id: str) -> None:
        booking = self._bookings.pop(booking_id, None)
        if booking is not None:
            booking.vehicle.is_booked.set(False)

    def get_all_bookings(self) -> List[Booking]:
        return list(self._bookings.values())
