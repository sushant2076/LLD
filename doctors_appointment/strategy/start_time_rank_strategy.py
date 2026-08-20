from examples.doctors_appointment.dto.doctor_slot import DoctorSlot
from examples.doctors_appointment.strategy.slot_rank_strategy import SlotRankStrategy
from examples.doctors_appointment.utils.utils import convert_string_to_local_time


class StartTimeRankStrategy(SlotRankStrategy):
    """Ranks slots by ascending start time."""

    def rank(self, slots: list[DoctorSlot]) -> list[DoctorSlot]:
        slots.sort(key=lambda slot: convert_string_to_local_time(slot.slot))
        return slots
