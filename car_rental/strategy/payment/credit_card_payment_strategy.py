from examples.car_rental.model.booking import Booking
from examples.car_rental.strategy.payment.payment_strategy import PaymentStrategy


class CreditCardPaymentStrategy(PaymentStrategy):
    def process_payment(self, booking: Booking) -> bool:
        # Simulate credit card processing
        print(f"Processing credit card payment for booking: {booking.booking_id}")
        return True
