"""DebtSimplificationService: collapses a web of pairwise balances within a
group down to a minimal set of settle-up transactions."""

import heapq
import itertools

from examples.splitwise.model.group import Group
from examples.splitwise.model.user import User


class DebtSimplificationService:
    def simplify_debts(self, group: Group) -> None:
        users = list(group.members)
        sheets = group.balance_sheets

        # Step 1: Calculate net balances for each user.
        net_balances: dict[User, float] = {}
        for user in users:
            net = sum(sheets[user].balances.values())
            net_balances[user] = net
            sheets[user].clear_balances()  # Clear old balances before recomputing.

        # Step 2: Separate creditors (net > 0) and debtors (net < 0).
        # Python's heapq is a min-heap, so creditors (who need max-first order)
        # are pushed with a negated key.
        counter = itertools.count()  # tie-breaker to avoid comparing User objects
        creditors: list[tuple[float, int, User]] = []
        debtors: list[tuple[float, int, User]] = []

        for user in users:
            net = net_balances[user]
            if net > 0:
                heapq.heappush(creditors, (-net, next(counter), user))
            elif net < 0:
                heapq.heappush(debtors, (net, next(counter), user))

        # Step 3: Match debtors and creditors to settle debts.
        while creditors and debtors:
            neg_credit_amount, _, creditor = heapq.heappop(creditors)
            debit_amount, _, debtor = heapq.heappop(debtors)
            credit_amount = -neg_credit_amount

            settled_amount = min(credit_amount, -debit_amount)

            # Update balances on both sides.
            sheets[creditor].add_balance(debtor, settled_amount)
            sheets[debtor].add_balance(creditor, -settled_amount)

            # Update net balances after settlement.
            net_balances[creditor] = credit_amount - settled_amount
            net_balances[debtor] = debit_amount + settled_amount

            # If still unsettled, re-add to the heaps.
            if net_balances[creditor] > 0:
                heapq.heappush(
                    creditors, (-net_balances[creditor], next(counter), creditor)
                )
            if net_balances[debtor] < 0:
                heapq.heappush(
                    debtors, (net_balances[debtor], next(counter), debtor)
                )
