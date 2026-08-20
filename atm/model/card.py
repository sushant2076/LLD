from dataclasses import dataclass

from examples.atm.model.account import Account


@dataclass(frozen=True)
class Card:
    """An ATM card, linked to a single account."""

    card_number: str
    pin: str
    account: Account
