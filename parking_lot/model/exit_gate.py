from datetime import datetime

from ..enums.gate_type import GateType
from ..enums.payment_mode import PaymentMode
from .gate import Gate


class ExitGate(Gate):
    """Mirrors ExitGate.java."""

    def __init__(self, id: str):
        super().__init__(id)

    @property
    def type(self) -> GateType:
        return GateType.EXIT

    def unpark_vehicle(self, ticket_id: str, exit_time: datetime, payment_mode: PaymentMode) -> None:
        # Local import to avoid a circular import between model and service packages.
        from ..service.parking_lot import ParkingLot

        ParkingLot.get_instance().unpark_vehicle(ticket_id, exit_time, payment_mode)
