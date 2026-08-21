"""GroupService: the top-level facade used by clients to create groups, add
expenses, simplify debts and print balances."""

import uuid

from splitwise.enums.split_type import SplitType
from splitwise.model.group import Group
from splitwise.model.user import User
from splitwise.repository.group_repository import GroupRepository
from splitwise.service.debt_simplification_service import (
    DebtSimplificationService,
)
from splitwise.service.expense_service import ExpenseService


class GroupService:
    def __init__(
        self,
        repo: GroupRepository,
        expense_service: ExpenseService,
        simplifier: DebtSimplificationService,
    ) -> None:
        self.repo = repo
        self.expense_service = expense_service
        self.simplifier = simplifier

    def create_group(self, name: str, members: list[User]) -> str:
        id = str(uuid.uuid4())
        group = Group(id, name)
        for member in members:
            group.add_member(member)

        self.repo.save(group)
        return id

    def add_member(self, group_id: str, user: User) -> None:
        self._get(group_id).add_member(user)

    def add_expense(
        self,
        group_id: str,
        description: str,
        amount: float,
        paid_by: User,
        participants: list[User],
        split_type: SplitType,
        meta: dict[User, float] | None,
    ) -> None:
        self.expense_service.add_expense(
            self._get(group_id), description, amount, paid_by, participants,
            split_type, meta,
        )

    def simplify_debts(self, group_id: str) -> None:
        self.simplifier.simplify_debts(self._get(group_id))

    def print_balances(self, group_id: str) -> None:
        group = self._get(group_id)
        for user in group.members:
            sheet = group.get_balance_sheet(user)

            owe = 0.0
            get = 0.0
            for v in sheet.balances.values():
                if v < 0:
                    owe += -v
                else:
                    get += v

            print(
                f"\U0001F4B5 {user.name}\n"
                f"Paid: {sheet.total_paid:.2f}  Expense: {sheet.total_expense:.2f}\n"
                f"You owe: {owe:.2f}, You get: {get:.2f}"
            )

            for other, val in sheet.balances.items():
                arrow = "← get" if val > 0 else "→ owe"
                print(f"  {arrow} {abs(val):.2f} {other.name}")
            print("--------------------------")

    def _get(self, id: str) -> Group:
        group = self.repo.find_by_id(id)
        if group is None:
            raise ValueError(f"Group not found: {id}")
        return group
