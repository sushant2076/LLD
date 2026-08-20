from enum import Enum, auto


class VehicleStatus(Enum):
    AVAILABLE = auto()  # Default, available to be booked if no booking conflict
    BOOKED = auto()
    IN_SERVICE = auto()  # Under maintenance
    DECOMMISSIONED = auto()  # Removed from fleet
