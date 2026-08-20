"""Group model: a collection of users sharing expenses."""

from examples.splitwise.model.balance_sheet import BalanceSheet
from examples.splitwise.model.expense import Expense
from examples.splitwise.model.user import User


class Group:
    def __init__(self, id: str, name: str) -> None:
        self.id = id
        self.name = name
        self.members: list[User] = []
        self.expenses: list[Expense] = []
        self.balance_sheets: dict[User, BalanceSheet] = {}

    def add_member(self, user: User) -> None:
        self.members.append(user)
        self.balance_sheets.setdefault(user, BalanceSheet())

    def add_expense(self, expense: Expense) -> None:
        self.expenses.append(expense)

    def get_balance_sheet(self, user: User) -> BalanceSheet:
        return self.balance_sheets[user]
