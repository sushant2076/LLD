import uuid
from collections import deque

from doctors_appointment.model.booking import Booking


class BookingRepository:
    """In-memory storage for bookings and per-slot waitlists."""

    def __init__(self) -> None:
        self.booking_map: dict[uuid.UUID, Booking] = {}
        # key ("<doctor_id>-<slot>") -> queue of patient ids
        self.waitlist: dict[str, deque[uuid.UUID]] = {}

    def save(self, booking: Booking) -> None:
        self.booking_map[booking.id] = booking

    def delete(self, booking: Booking) -> None:
        self.booking_map.pop(booking.id, None)

    def get_booking_by_id(self, booking_id: uuid.UUID) -> Booking | None:
        return self.booking_map.get(booking_id)

    def find_by_doctor(self, doctor_id: uuid.UUID) -> list[Booking]:
        return [b for b in self.booking_map.values() if b.doctor_id == doctor_id]

    def find_by_patient(self, patient_id: uuid.UUID) -> list[Booking]:
        return [b for b in self.booking_map.values() if b.patient_id == patient_id]

    def add_to_waitlist(self, doctor_slot_key: str, patient_id: uuid.UUID) -> None:
        self.waitlist.setdefault(doctor_slot_key, deque()).append(patient_id)

    def pop_from_waitlist(self, doctor_slot_key: str) -> uuid.UUID | None:
        queue = self.waitlist.get(doctor_slot_key)
        if not queue:
            return None
        return queue.popleft()
