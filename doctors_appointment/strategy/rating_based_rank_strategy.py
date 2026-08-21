from doctors_appointment.dto.doctor_slot import DoctorSlot
from doctors_appointment.strategy.slot_rank_strategy import SlotRankStrategy


class RatingBasedRankStrategy(SlotRankStrategy):
    """Ranks slots by descending doctor rating."""

    def rank(self, slots: list[DoctorSlot]) -> list[DoctorSlot]:
        slots.sort(key=lambda slot: slot.doctor.rating, reverse=True)
        return slots
