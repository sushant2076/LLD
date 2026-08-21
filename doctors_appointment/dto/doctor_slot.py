from dataclasses import dataclass

from doctors_appointment.model.doctor import Doctor


@dataclass(frozen=True)
class DoctorSlot:
    doctor: Doctor
    slot: str
