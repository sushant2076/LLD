from examples.car_rental.model.booking import Booking
from examples.car_rental.strategy.payment.payment_strategy import PaymentStrategy


class WalletPaymentStrategy(PaymentStrategy):
    def process_payment(self, booking: Booking) -> bool:
        # Simulate wallet payment processing
        print(f"Processing wallet payment for booking: {booking.booking_id}")
        return True
