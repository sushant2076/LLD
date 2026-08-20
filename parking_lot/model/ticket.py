from dataclasses import dataclass
from datetime import datetime

from ..enums.payment_status import PaymentStatus
from .vehicle import Vehicle


@dataclass
class Ticket:
    """Mirrors Ticket.java (Lombok @Data @Builder)."""

    ticket_id: str
    entry_time: datetime
    vehicle: Vehicle
    floor_id: str
    spot_id: str
    payment_status: PaymentStatus = PaymentStatus.PENDING
