from abc import ABC, abstractmethod

from ...model.ticket import Ticket


class PaymentStrategy(ABC):
    """Mirrors PaymentStrategy.java interface."""

    @abstractmethod
    def process_payment(self, ticket: Ticket, amount: float) -> bool:
        raise NotImplementedError
