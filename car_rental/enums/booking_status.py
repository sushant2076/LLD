from enum import Enum, auto


class BookingStatus(Enum):
    CREATED = auto()
    CONFIRMED = auto()
    COMPLETED = auto()
    CANCELLED = auto()
    FAILED = auto()
