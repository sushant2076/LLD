import uuid

from examples.doctors_appointment.exception.patient_not_found_exception import (
    PatientNotFoundException,
)
from examples.doctors_appointment.model.patient import Patient
from examples.doctors_appointment.repository.patient_repository import (
    PatientRepository,
)


class PatientService:
    def __init__(self, repo: PatientRepository) -> None:
        self.repo = repo

    def register(self, name: str) -> Patient:
        patient = Patient(name)
        self.repo.save(patient)
        return patient

    def find_by_id(self, patient_id: uuid.UUID) -> Patient:
        patient = self.repo.find_by_id(patient_id)
        if patient is None:
            raise PatientNotFoundException("Patient not found")
        return patient
