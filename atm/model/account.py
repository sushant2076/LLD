from dataclasses import dataclass


@dataclass
class Account:
    """A bank account tied to a card."""

    account_number: str
    balance: float
