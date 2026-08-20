from __future__ import annotations
from datetime import datetime

from ..enums.gate_type import GateType
from .gate import Gate
from .ticket import Ticket
from .vehicle import Vehicle


class EntryGate(Gate):
    """Mirrors EntryGate.java."""

    def __init__(self, id: str):
        super().__init__(id)

    @property
    def type(self) -> GateType:
        return GateType.ENTRY

    def park_vehicle(self, vehicle: Vehicle, entry_time: datetime) -> Ticket | None:
        # Local import to avoid a circular import between model and service packages.
        from ..service.parking_lot import ParkingLot

        return ParkingLot.get_instance().park_vehicle(vehicle, entry_time)
