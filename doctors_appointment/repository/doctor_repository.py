import uuid

from doctors_appointment.enums.specialization import Specialization
from doctors_appointment.model.doctor import Doctor


class DoctorRepository:
    """In-memory storage for doctors."""

    def __init__(self) -> None:
        self.doctor_map: dict[uuid.UUID, Doctor] = {}

    def save(self, doctor: Doctor) -> None:
        self.doctor_map[doctor.id] = doctor

    def find_by_id(self, doctor_id: uuid.UUID) -> Doctor | None:
        return self.doctor_map.get(doctor_id)

    def find_by_specialization(self, specialization: Specialization) -> list[Doctor]:
        return [
            doc
            for doc in self.doctor_map.values()
            if doc.specialization == specialization
        ]
