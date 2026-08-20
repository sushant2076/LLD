import uuid
from dataclasses import dataclass, field


@dataclass
class Patient:
    name: str
    id: uuid.UUID = field(default_factory=uuid.uuid4, init=False)
