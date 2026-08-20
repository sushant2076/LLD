"""Split model: how much a single user owes for a particular expense."""

from dataclasses import dataclass

from examples.splitwise.model.user import User


@dataclass
class Split:
    user: User
    amount: float
