"""ExpenseService: creates an Expense using the appropriate SplitStrategy and
records it against the group's balance sheets."""

from splitwise.enums.split_type import SplitType
from splitwise.factory.split_strategy_factory import SplitStrategyFactory
from splitwise.model.expense import Expense
from splitwise.model.group import Group
from splitwise.model.user import User
from splitwise.service.balance_sheet_service import BalanceSheetService


class ExpenseService:
    def __init__(self, balance_sheet_service: BalanceSheetService) -> None:
        self.balance_sheet_service = balance_sheet_service

    def add_expense(
        self,
        group: Group,
        description: str,
        amount: float,
        paid_by: User,
        participants: list[User],
        split_type: SplitType,
        metadata: dict[User, float] | None,
    ) -> None:
        strategy = SplitStrategyFactory.get_strategy(split_type)
        splits = strategy.split(amount, participants, metadata)
        expense = Expense(description, amount, paid_by, splits, split_type)
        group.add_expense(expense)

        self.balance_sheet_service.update_balances(group, paid_by, splits)
