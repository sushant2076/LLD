from abc import ABC, abstractmethod

from car_rental.model.booking import Booking


class PaymentStrategy(ABC):
    @abstractmethod
    def process_payment(self, booking: Booking) -> bool:
        raise NotImplementedError
