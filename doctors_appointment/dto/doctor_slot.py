from dataclasses import dataclass

from examples.doctors_appointment.model.doctor import Doctor


@dataclass(frozen=True)
class DoctorSlot:
    doctor: Doctor
    slot: str
