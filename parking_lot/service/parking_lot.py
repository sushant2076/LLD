from __future__ import annotations
import threading
import uuid
from datetime import datetime
from typing import ClassVar, Optional

from ..enums.payment_mode import PaymentMode
from ..enums.pricing_strategy_type import PricingStrategyType
from ..factory.payment_strategy_factory import PaymentStrategyFactory
from ..factory.pricing_strategy_factory import PricingStrategyFactory
from ..model.parking_floor import ParkingFloor
from ..model.ticket import Ticket
from ..model.vehicle import Vehicle
from ..strategy.pricing.pricing_strategy import PricingStrategy
from .payment_processor import PaymentProcessor


class ParkingLot:
    """Mirrors ParkingLot.java, a classic (thread-safe) singleton."""

    _instance: ClassVar[Optional["ParkingLot"]] = None
    _instance_lock: ClassVar[threading.Lock] = threading.Lock()

    def __init__(self) -> None:
        self.floors: dict[str, ParkingFloor] = {}
        self.active_tickets: dict[str, Ticket] = {}
        self._tickets_lock = threading.Lock()
        self.pricing_strategy: PricingStrategy = PricingStrategyFactory.get(PricingStrategyType.TIME_BASED)

    @classmethod
    def xget_instance(cls) -> "ParkingLot":
        if cls._instance is None:
            with cls._instance_lock:
                if cls._instance is None:
                    cls._instance = cls()
        return cls._instance

    def add_floor(self, floor: ParkingFloor) -> None:
        self.floors[floor.id] = floor

    def park_vehicle(self, vehicle: Vehicle, entry_time: datetime) -> Optional[Ticket]:
        for floor in self.floors.values():
            spot = floor.find_available_spot(vehicle.type)

            if spot is not None:
                # Successfully reserved the spot via an atomic operation.
                ticket_id = str(uuid.uuid4())
                ticket = Ticket(
                    ticket_id=ticket_id,
                    entry_time=entry_time,
                    vehicle=vehicle,
                    floor_id=floor.id,
                    spot_id=spot.id,
                )

                with self._tickets_lock:
                    self.active_tickets[ticket_id] = ticket
                print(f"Vehicle parked. Ticket: {ticket_id}")
                return ticket

        print(f"No spot available for vehicle type: {vehicle.type}")
        return None

    def unpark_vehicle(self, ticket_id: str, exit_time: datetime, payment_mode: PaymentMode) -> None:
        ticket = self.active_tickets.get(ticket_id)
        if ticket is None:
            print("Invalid ticket ID.")
            return

        fee = self.pricing_strategy.calculate_fee(
            ticket.vehicle.type,
            ticket.entry_time,
            exit_time,
        )

        strategy = PaymentStrategyFactory.get(payment_mode)
        processor = PaymentProcessor(strategy)
        paid = processor.pay(ticket, fee)

        if not paid:
            print("Vehicle cannot exit. Payment unsuccessful.")
            return

        spot = self.floors[ticket.floor_id].spots[ticket.spot_id]
        spot.vacate()
        with self._tickets_lock:
            self.active_tickets.pop(ticket_id, None)

        print(f"Vehicle exited. Fee charged: ₹{fee}")

    def print_status(self) -> None:
        for floor_id, floor in self.floors.items():
            print(f"Floor: {floor_id}")
            for spot in floor.spots.values():
                status = "Occupied" if spot.is_occupied() else "Free"
                print(f" Spot {spot.id} [{spot.allowed_type}] - {status}")
