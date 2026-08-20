"""Demo entry point mirroring Main.java's end-to-end flow.

Exercises: park a vehicle -> get a ticket -> inspect status -> unpark with
payment -> inspect status again.
"""

from .enums.payment_mode import PaymentMode
from .enums.pricing_strategy_type import PricingStrategyType
from .enums.vehicle_type import VehicleType
from .factory.pricing_strategy_factory import PricingStrategyFactory
from .factory.vehicle_factory import VehicleFactory
from .model.entry_gate import EntryGate
from .model.exit_gate import ExitGate
from .model.parking_floor import ParkingFloor
from .model.parking_spot import ParkingSpot
from .service.parking_lot import ParkingLot
from .utils.date_time_parser import DateTimeParser


def main() -> None:
    lot = ParkingLot.get_instance()
    entry_gate = EntryGate("EG1")
    exit_gate = ExitGate("XG1")

    lot.pricing_strategy = PricingStrategyFactory.get(PricingStrategyType.EVENT_BASED)

    floor1 = ParkingFloor("Floor1")
    floor1.add_spot(ParkingSpot("F1S1", VehicleType.BIKE))
    floor1.add_spot(ParkingSpot("F1S2", VehicleType.CAR))
    floor1.add_spot(ParkingSpot("F1S3", VehicleType.TRUCK))
    floor1.add_spot(ParkingSpot("F1S4", VehicleType.CAR))
    lot.add_floor(floor1)

    print("--------------------------")

    car = VehicleFactory.create("KA01AB1234", VehicleType.CAR)

    entry_time = DateTimeParser.parse("21 May 7:30 AM 2025")
    ticket = entry_gate.park_vxxehicle(car, entry_time)

    print("--------------------------")

    lot.print_status()

    print("--------------------------")

    exit_time = DateTimeParser.parse("21 May 1:15 PM 2025")
    exit_gate.unpark_vehicle(ticket.ticket_id, exit_time, PaymentMode.UPI)

    print("--------------------------")

    lot.print_status()


if __name__ == "__main__":
    main()
