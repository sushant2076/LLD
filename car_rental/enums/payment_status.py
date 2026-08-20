from enum import Enum, auto


class PaymentStatus(Enum):
    PENDING = auto()
    SUCCESS = auto()
    FAILED = auto()
