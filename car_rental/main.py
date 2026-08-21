"""Demo entry point for the car rental LLD example.

Mirrors org.nailyourinterview.lld.car_rental.Main: sets up branches and vehicles,
concurrently books a vehicle from two threads (only one should win), then returns
the booked vehicle to its drop branch.
"""

import threading

from car_rental.enums.vehicle_type import VehicleType
from car_rental.factory.vehicle_factory import VehicleFactory
from car_rental.model.branch import Branch
from car_rental.model.user import User
from car_rental.repository.booking_repository import BookingRepository
from car_rental.repository.branch_repository import BranchRepository
from car_rental.service.booking_service import BookingService
from car_rental.strategy.booking.least_booked_vehicle_strategy import (
    LeastBookedVehicleStrategy,
)
from car_rental.strategy.payment.credit_card_payment_strategy import (
    CreditCardPaymentStrategy,
)
from car_rental.strategy.payment.wallet_payment_strategy import (
    WalletPaymentStrategy,
)
from car_rental.strategy.pricing.hourly_pricing_strategy import (
    HourlyPricingStrategy,
)
from car_rental.utils.date_time_parser import DateTimeParser


def main() -> None:
    branch_repo = BranchRepository()
    booking_repo = BookingRepository()

    branch1 = Branch("B1", "New York")
    branch2 = Branch("B2", "Boston")
    branch_repo.add_branch(branch1)
    branch_repo.add_branch(branch2)

    branch1.add_vehicle(VehicleFactory.create(VehicleType.SEDAN, "NY1234", 25, 3.5))
    branch1.add_vehicle(VehicleFactory.create(VehicleType.SEDAN, "NY5678", 22, 3))
    branch1.add_vehicle(VehicleFactory.create(VehicleType.SUV, "NYB100", 30, 4))

    branch2.add_vehicle(VehicleFactory.create(VehicleType.SEDAN, "BO1234", 25, 4))

    user = User("U1", "John Doe", "john@example.com")

    start = DateTimeParser.parse("21 May 7:30 AM 2025")
    end = DateTimeParser.parse("21 May 12:30 PM 2025")

    booking_service = BookingService.get_instance(
        branch_repo,
        booking_repo,
        LeastBookedVehicleStrategy(),
        HourlyPricingStrategy(),
    )

    print("--------------")

    results = {}

    def book(name: str, payment_strategy) -> None:
        print(f"{name} started!")
        results[name] = booking_service.book_vehicle(
            "B1",
            VehicleType.SUV,
            start,
            end,
            user,
            payment_strategy,
            branch1,
            branch2,
            100.0,
        )
        print(f"{name} ended!")

    t1 = threading.Thread(target=book, args=("Thread-1", CreditCardPaymentStrategy()))
    t2 = threading.Thread(target=book, args=("Thread-2", WalletPaymentStrategy()))

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("--------------")

    # Return the vehicle for whichever thread's booking succeeded.
    successful_booking = results.get("Thread-1") or results.get("Thread-2")
    if successful_booking is not None:
        booking_service.return_vehicle(successful_booking.booking_id)


if __name__ == "__main__":
    main()
