import uuid

from examples.doctors_appointment.dto.doctor_slot import DoctorSlot
from examples.doctors_appointment.enums.specialization import Specialization
from examples.doctors_appointment.exception.booking_not_found_exception import (
    BookingNotFoundException,
)
from examples.doctors_appointment.model.booking import Booking
from examples.doctors_appointment.repository.booking_repository import (
    BookingRepository,
)
from examples.doctors_appointment.repository.doctor_repository import (
    DoctorRepository,
)
from examples.doctors_appointment.repository.patient_repository import (
    PatientRepository,
)
from examples.doctors_appointment.strategy.slot_rank_strategy import (
    SlotRankStrategy,
)


class BookingService:
    def __init__(
        self,
        booking_repo: BookingRepository,
        doctor_repo: DoctorRepository,
        patient_repo: PatientRepository,
    ) -> None:
        self.booking_repo = booking_repo
        self.doctor_repo = doctor_repo
        self.patient_repo = patient_repo

    def search(
        self, spec: Specialization, strategy: SlotRankStrategy
    ) -> list[DoctorSlot]:
        doctors = self.doctor_repo.find_by_specialization(spec)
        result: list[DoctorSlot] = []

        for doctor in doctors:
            for slot, is_available in doctor.availability.items():
                if is_available:
                    result.append(DoctorSlot(doctor, slot))
        return strategy.rank(result)

    def book(
        self, patient_id: uuid.UUID, doctor_id: uuid.UUID, slot: str
    ) -> Booking:
        doctor = self.doctor_repo.find_by_id(doctor_id)
        availability = doctor.availability

        # Slot not declared
        if slot not in availability:
            raise RuntimeError(
                "Invalid slot: Doctor has not declared availability for this slot."
            )

        # Patient already has a booking in this slot
        for booking in self.booking_repo.find_by_patient(patient_id):
            if booking.slot == slot:
                raise RuntimeError("Patient already has an appointment at this time")

        # Book if slot is available
        if availability[slot]:
            booking = Booking(patient_id, doctor_id, slot)
            self.booking_repo.save(booking)
            availability[slot] = False  # mark slot as booked

            print(
                f"\n{self.patient_repo.find_by_id(patient_id).name} "
                f"booked a slot successfully for slot : {slot}"
            )

            return booking
        else:
            # Add to waitlist if valid but booked
            key = f"{doctor_id}-{slot}"
            self.booking_repo.add_to_waitlist(key, patient_id)
            raise RuntimeError("Slot already booked. Added to waitlist.")

    def cancel(self, booking_id: uuid.UUID) -> None:
        booking = self.booking_repo.get_booking_by_id(booking_id)
        if booking is None:
            raise BookingNotFoundException("Booking not found")

        doctor = self.doctor_repo.find_by_id(booking.doctor_id)
        doctor.availability[booking.slot] = True  # mark slot as available
        self.booking_repo.delete(booking)

        print(
            f"\n{self.patient_repo.find_by_id(booking.patient_id).name} "
            f"cancelled the booking for slot : {booking.slot}"
        )

        # Promote first patient in waitlist
        key = f"{doctor.id}-{booking.slot}"
        next_patient = self.booking_repo.pop_from_waitlist(key)
        if next_patient is not None:
            self.book(next_patient, doctor.id, booking.slot)

    def view_bookings_by_doctor(self, doctor_id: uuid.UUID) -> list[Booking]:
        return self.booking_repo.find_by_doctor(doctor_id)

    def view_bookings_by_patient(self, patient_id: uuid.UUID) -> list[Booking]:
        return self.booking_repo.find_by_patient(patient_id)
