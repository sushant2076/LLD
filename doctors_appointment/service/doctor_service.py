import uuid

from doctors_appointment.enums.specialization import Specialization
from doctors_appointment.exception.doctor_not_found_exception import (
    DoctorNotFoundException,
)
from doctors_appointment.model.doctor import Doctor
from doctors_appointment.repository.doctor_repository import (
    DoctorRepository,
)


class DoctorService:
    def __init__(self, repo: DoctorRepository) -> None:
        self.repo = repo

    def register(
        self, name: str, spec: Specialization, rating: float
    ) -> Doctor:
        doctor = Doctor(name, spec, rating)
        self.repo.save(doctor)
        return doctor

    def declare_availability(self, doctor_id: uuid.UUID, slots: list[str]) -> None:
        doc = self.repo.find_by_id(doctor_id)
        if doc is None:
            raise DoctorNotFoundException("Doctor not found")
        for slot in slots:
            doc.availability[slot] = True
