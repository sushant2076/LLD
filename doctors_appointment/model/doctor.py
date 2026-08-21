import uuid
from dataclasses import dataclass, field

from doctors_appointment.enums.specialization import Specialization


@dataclass
class Doctor:
    name: str
    specialization: Specialization
    rating: float
    id: uuid.UUID = field(default_factory=uuid.uuid4, init=False)
    # slot -> is_available
    availability: dict[str, bool] = field(default_factory=dict, init=False)
