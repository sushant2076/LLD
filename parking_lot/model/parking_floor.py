from __future__ import annotations
from typing import Optional

from ..enums.vehicle_type import VehicleType
from .parking_spot import ParkingSpot


class ParkingFloor:
    """Mirrors ParkingFloor.java."""

    def __init__(self, id: str):
        self.id = id
        self.spots: dict[str, ParkingSpot] = {}

    def add_spot(self, spot: ParkingSpot) -> None:
        self.spots[spot.id] = spot

    def find_available_spot(self, vehicle_type: VehicleType) -> Optional[ParkingSpot]:
        for spot in self.spots.values():
            if spot.allowed_type == vehicle_type and spot.try_occupy():
                return spot
        return None
