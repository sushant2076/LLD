from abc import ABC, abstractmethod

from examples.doctors_appointment.dto.doctor_slot import DoctorSlot


class SlotRankStrategy(ABC):
    """Strategy interface for ranking/ordering available doctor slots."""

    @abstractmethod
    def rank(self, slots: list[DoctorSlot]) -> list[DoctorSlot]:
        raise NotImplementedError
