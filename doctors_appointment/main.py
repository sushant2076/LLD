from doctors_appointment.enums.specialization import Specialization
from doctors_appointment.repository.booking_repository import (
    BookingRepository,
)
from doctors_appointment.repository.doctor_repository import (
    DoctorRepository,
)
from doctors_appointment.repository.patient_repository import (
    PatientRepository,
)
from doctors_appointment.service.booking_service import BookingService
from doctors_appointment.service.doctor_service import DoctorService
from doctors_appointment.service.patient_service import PatientService
from doctors_appointment.strategy.start_time_rank_strategy import (
    StartTimeRankStrategy,
)


def main() -> None:
    doctor_repository = DoctorRepository()
    patient_repository = PatientRepository()
    booking_repository = BookingRepository()

    doctor_service = DoctorService(doctor_repository)
    patient_service = PatientService(patient_repository)
    booking_service = BookingService(
        booking_repository, doctor_repository, patient_repository
    )
    rank_strategy = StartTimeRankStrategy()

    # Register doctors
    curious = doctor_service.register("Curious", Specialization.CARDIOLOGIST, 4.5)
    dreadful = doctor_service.register("Dreadful", Specialization.CARDIOLOGIST, 3.8)
    doctor_service.register("Daring", Specialization.DERMATOLOGIST, 4.2)

    # Declare availability
    doctor_service.declare_availability(curious.id, ["9:30", "12:30", "16:00"])
    doctor_service.declare_availability(dreadful.id, ["12:30", "13:00"])

    # Register patients
    p1 = patient_service.register("Shubh")
    p2 = patient_service.register("Kunal")

    # Search slots
    print("Available Cardiologist slots:")
    slots = booking_service.search(Specialization.CARDIOLOGIST, rank_strategy)
    for slot in slots:
        print(f"{slot.doctor.name} - {slot.slot}")

    # Book slots
    b1 = booking_service.book(p1.id, curious.id, "12:30")

    # Bookings of Doctor Curious
    print("\nDoctor Curious bookings:")
    for b in booking_service.view_bookings_by_doctor(curious.id):
        patient_name = patient_service.find_by_id(b.patient_id).name
        print(f"Booking: Patient ID {patient_name}, Slot {b.slot}")

    # Try booking same slot for another patient
    try:
        booking_service.book(p2.id, curious.id, "12:30")
    except Exception as e:  # noqa: BLE001 - mirrors broad catch in Java source
        print(f"\nPatient 2 waitlisted: {e}")

    # Cancel booking and observe waitlist trigger
    booking_service.cancel(b1.id)

    # Final bookings
    print("\nDoctor Curious bookings:")
    for b in booking_service.view_bookings_by_doctor(curious.id):
        patient_name = patient_service.find_by_id(b.patient_id).name
        print(f"Booking: Patient ID {patient_name}, Slot {b.slot}")


if __name__ == "__main__":
    main()
