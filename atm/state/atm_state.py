from abc import ABC, abstractmethod

from atm.enums.atm_status import ATMStatus
from atm.model.card import Card


class ATMState(ABC):
    """State pattern interface for the ATM's operational states."""

    @abstractmethod
    def insert_card(self, card: Card) -> None:
        ...

    @abstractmethod
    def enter_pin(self, pin: str) -> None:
        ...

    @abstractmethod
    def select_option(self, option: str) -> None:
        ...

    @abstractmethod
    def dispense_cash(self, amount: int) -> None:
        ...

    @abstractmethod
    def eject_card(self) -> None:
        ...

    @property
    @abstractmethod
    def status(self) -> ATMStatus:
        ...
