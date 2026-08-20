import uuid
from dataclasses import dataclass, field


@dataclass
class Booking:
    patient_id: uuid.UUID
    doctor_id: uuid.UUID
    slot: str
    id: uuid.UUID = field(default_factory=uuid.uuid4, init=False)
