import uuid

from examples.doctors_appointment.model.patient import Patient


class PatientRepository:
    """In-memory storage for patients."""

    def __init__(self) -> None:
        self.patient_map: dict[uuid.UUID, Patient] = {}

    def save(self, patient: Patient) -> None:
        self.patient_map[patient.id] = patient

    def find_by_id(self, patient_id: uuid.UUID) -> Patient | None:
        return self.patient_map.get(patient_id)
