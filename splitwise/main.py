"""Demo entry point, ported from the original Java Main class.

Exercises adding an expense with each split type (equal, percentage, exact)
and prints the resulting balances.
"""

from splitwise.enums.split_type import SplitType
from splitwise.model.user import User
from splitwise.repository.in_memory_group_repository import (
    InMemoryGroupRepository,
)
from splitwise.service.balance_sheet_service import BalanceSheetService
from splitwise.service.debt_simplification_service import (
    DebtSimplificationService,
)
from splitwise.service.expense_service import ExpenseService
from splitwise.service.group_service import GroupService


def main() -> None:
    # users
    shubh = User("u1", "Shubh")
    bob = User("u2", "Bob")
    tom = User("u3", "Tom")
    jake = User("u4", "Jake")

    repo = InMemoryGroupRepository()
    balance_sheet_service = BalanceSheetService()
    expense_service = ExpenseService(balance_sheet_service)
    simplification_service = DebtSimplificationService()

    group_service = GroupService(repo, expense_service, simplification_service)

    # ---------- create groups ----------
    goa_group_id = group_service.create_group("Goa Trip", [shubh, bob, tom, jake])

    # ---------- add expenses (one per split type) ----------
    group_service.add_expense(
        goa_group_id,
        "Lunch Day-1", 100, shubh,
        [shubh, bob], SplitType.EQUAL, None,
    )

    group_service.add_expense(
        goa_group_id,
        "Lunch Day-2", 100, bob,
        [bob, tom], SplitType.EQUAL, None,
    )

    group_service.add_expense(
        goa_group_id,
        "Hotel", 300, shubh,
        [shubh, bob, tom],
        SplitType.PERCENTAGE,
        {shubh: 50.0, bob: 30.0, tom: 20.0},
    )

    group_service.add_expense(
        goa_group_id,
        "Taxi", 90, tom,
        [tom, jake, shubh],
        SplitType.EXACT,
        {tom: 30.0, jake: 40.0, shubh: 20.0},
    )

    print("=== Balances before simplification ===")
    group_service.print_balances(goa_group_id)

    # ---------- simplify & print ----------
    group_service.simplify_debts(goa_group_id)

    print("=== Balances after simplification ===")
    group_service.print_balances(goa_group_id)


if __name__ == "__main__":
    main()
