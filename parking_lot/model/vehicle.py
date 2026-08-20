from abc import ABC
from dataclasses import dataclass

from ..enums.vehicle_type import VehicleType


@dataclass(frozen=True)
class Vehicle(ABC):
    """Base class for all vehicles. Mirrors Vehicle.java (Lombok @Getter @RequiredArgsConstructor)."""

    number: str
    type: VehicleType
