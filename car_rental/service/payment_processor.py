from examples.car_rental.enums.payment_status import PaymentStatus
from examples.car_rental.model.booking import Booking
from examples.car_rental.strategy.payment.payment_strategy import PaymentStrategy


class PaymentProcessor:
    def __init__(self, payment_strategy: PaymentStrategy):
        self.payment_strategy = payment_strategy

    def pay(self, booking: Booking) -> bool:
        success = self.payment_strategy.process_payment(booking)

        if success:
            booking.payment_status = PaymentStatus.SUCCESS
        else:
            booking.payment_status = PaymentStatus.FAILED
            print("Payment Failed!")

        return success
