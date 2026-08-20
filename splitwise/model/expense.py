"""Expense model."""

from dataclasses import dataclass, field

from examples.splitwise.enums.split_type import SplitType
from examples.splitwise.model.split import Split
from examples.splitwise.model.user import User


@dataclass(frozen=True)
class Expense:
    description: str
    amount: float
    paid_by: User
    splits: list[Split] = field(default_factory=list)
    split_type: SplitType = SplitType.EQUAL
