import threading
from abc import ABC

from car_rental.enums.vehicle_status import VehicleStatus
from car_rental.enums.vehicle_type import VehicleType


class AtomicBoolean:
    """A minimal thread-safe boolean flag, mirroring java.util.concurrent.atomic.AtomicBoolean."""

    def __init__(self, initial_value: bool = False):
        self._value = initial_value
        self._lock = threading.Lock()

    def get(self) -> bool:
        with self._lock:
            return self._value

    def set(self, value: bool) -> None:
        with self._lock:
            self._value = value

    def compare_and_set(self, expected: bool, new_value: bool) -> bool:
        with self._lock:
            if self._value == expected:
                self._value = new_value
                return True
            return False


class Vehicle(ABC):
    """Abstract base class for all rentable vehicles."""

    def __init__(self, license_plate: str, price_per_hour: float, price_per_km: float, vehicle_type: VehicleType):
        self.license_plate = license_plate
        self.status = VehicleStatus.AVAILABLE
        self.price_per_hour = price_per_hour
        self.price_per_km = price_per_km
        self.type = vehicle_type
        self.booking_count = 0
        self.is_booked = AtomicBoolean(False)

    def increment_booking_count(self) -> None:
        self.booking_count += 1

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(license_plate={self.license_plate!r}, status={self.status})"
