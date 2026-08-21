from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Optional

from atm.model.atm import ATM


class CashDispenser(ABC):
    """Chain-of-Responsibility link that can dispense a specific note denomination."""

    @abstractmethod
    def set_next_dispenser(self, next_dispenser: "CashDispenser") -> None:
        ...

    @abstractmethod
    def can_dispense(self, atm: ATM, amount: int) -> bool:
        ...

    @abstractmethod
    def dispense(self, atm: ATM, amount: int) -> None:
        ...
