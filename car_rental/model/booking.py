import uuid
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

from car_rental.enums.booking_status import BookingStatus
from car_rental.enums.payment_status import PaymentStatus
from car_rental.model.branch import Branch
from car_rental.model.user import User
from car_rental.model.vehicle import Vehicle


@dataclass
class Booking:
    user: User
    vehicle: Vehicle
    pickup_branch: Branch
    drop_branch: Branch
    start_time: datetime
    end_time: datetime
    amount: float
    booking_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    status: BookingStatus = BookingStatus.CREATED
    payment_status: PaymentStatus = PaymentStatus.PENDING

    def __str__(self) -> str:
        formatter = "%-d %b %I:%M %p %Y"
        pickup_time = self.start_time.strftime(formatter)
        drop_time = self.end_time.strftime(formatter)
        return (
            "\n"
            f"Booking ID: {self.booking_id}\n"
            f"User: {self.user.name if self.user else 'N/A'}\n"
            f"Pickup Time: {pickup_time}\n"
            f"Drop Time: {drop_time}\n"
            f"Pickup Location: {self.pickup_branch.city if self.pickup_branch else 'N/A'}\n"
            f"Drop Location: {self.drop_branch.city if self.drop_branch else 'N/A'}\n"
            f"Vehicle Type: {self.vehicle.type if self.vehicle else 'N/A'}\n"
            f"Vehicle Number Plate: {self.vehicle.license_plate if self.vehicle else 'N/A'}\n"
            f"Amount: ${self.amount:.2f}\n"
            f"Status: {self.status}\n"
        )
